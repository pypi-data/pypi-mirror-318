# mypy: disable-error-code="call-arg,attr-defined"

from pytest import mark, raises

from dataclasses import FrozenInstanceError
from typing import ClassVar, Protocol

from dataclass_baseclass import Data, DataClass, DataClassFrozen

from .conftest import DataClassTestFactory, ToStr


class P(Protocol):
    c_lst: ClassVar[list[str]] = ["Something"]
    _c_lst: ClassVar[list[str]] = ["Something"]

    s: str
    _s: str = "S"

    def gimme_s(self) -> str:
        return self.s


def test_mutable_class_vars() -> None:
    class WithClassVars(DataClass, P):
        c_d: ClassVar[dict[str, str]] = {"s": "Something"}

    class C(WithClassVars):
        c_t: ClassVar[tuple[str, str]] = ("s", "Something")
        c_s: ClassVar[set[str]] = {"Something"}

    wcv = C(s="S")  # type: ignore[abstract]
    assert wcv.c_lst == ["Something"]
    assert wcv.c_d == {"s": "Something"}
    assert wcv.c_t == ("s", "Something")
    assert wcv.c_s == {"Something"}
    assert wcv.s == "S"


def test_wrong_params() -> None:
    with raises(
        TypeError,
        match=r"dataclass\(\) got an unexpected keyword argument 'something'",
    ):

        class UnknownArg(
            DataClass, dataclass_params={"something": "whatever"}
        ):
            pass

    with raises(AssertionError, match=r"kw_only"):

        class KWOnly(DataClass, dataclass_params={"kw_only": False}):
            pass


def test_load_interface(dc_test_factory: DataClassTestFactory) -> None:
    _dc, loader = dc_test_factory()

    with raises(
        ValueError,
        match=r"strict mode not supported",
    ):
        loader(strict=True)


@mark.parametrize("frozen", [False, True])
def test_dataclass_base(
    dc_test_factory: DataClassTestFactory,
    test_data: Data,
    str_test_data: ToStr,
    frozen: bool,
) -> None:
    dc, loader = dc_test_factory(frozen, (P,))

    with raises(
        TypeError,
        match=r"C.__init__\(\) missing 1 required keyword-only argument:",
    ):
        e = loader()

    c_data = {**test_data["c"], **{"s": "Something"}}
    e = loader(c=c_data)
    assert e.gimme_s() == "what"
    assert e.d.gimme_s() == e.d.s
    assert e.c.gimme_s() == "Something"

    assert e._as_dict(public_only=False) == {
        "_s": e._s,
        "i": e.i,
        "s": e.s,
        "x": e.x,
        "ls": e.ls,
        "t": e.t,
        "game": e.game,
        "dct": e.dct,
        "c": {"_s": e.c._s, "i": e.c.i, "s": e.c.s},
        "d": {"_s": e.d._s, "i": e.d.i, "s": e.d.s},
    }
    assert e._as_dict() == {
        "i": e.i,
        "s": e.s,
        "x": e.x,
        "ls": e.ls,
        "t": e.t,
        "game": e.game,
        "dct": e.dct,
        "c": {"i": e.c.i, "s": e.c.s},
        "d": {"i": e.d.i, "s": e.d.s},
    }

    with raises(
        TypeError,
        match=r"__init__\(\) got an unexpected keyword argument 'unexpected_attr'",
    ):
        dc(i=1, unexpected_attr=True)

    data = str_test_data()
    e = dc(**data)
    assert e.gimme_s() == "what"
    assert type(e.c) is dict


def test_dataclass_mutable(dc_test_factory: DataClassTestFactory) -> None:
    _dc, loader = dc_test_factory(frozen=False)

    e = loader()

    e.i = 12


def test_dataclass_frozen(dc_test_factory: DataClassTestFactory) -> None:
    _dc, loader = dc_test_factory(frozen=True)

    e = loader()

    with raises(FrozenInstanceError, match=r"cannot assign to field"):
        e.i = 12


def test_frozen_mix() -> None:
    class C(DataClass):
        s: str = "Something"

    class CF(DataClassFrozen, C):
        pass

    cf = CF()
    with raises(FrozenInstanceError, match=r"cannot assign to field"):
        cf.s = ""

    class CUF(DataClass, CF):  # type: ignore[misc]
        pass

    cuf = CUF()
    with raises(FrozenInstanceError, match=r"cannot assign to field"):
        cuf.s = ""

    class CRUF(CUF, dataclass_params={"frozen": False}):
        pass

    cruf = CRUF()
    cruf.s = ""
    assert cruf.s == ""


def test_replace() -> None:
    class C(DataClass):
        s: str = "Something"

    c = C()
    with raises(
        TypeError,
        match=r"C.__init__\(\) got an unexpected keyword argument 'i'",
    ):
        c._replace(i=1)

    cr = c._replace(s="")
    assert cr.s == ""
    assert cr is not c


def test_protocol() -> None:
    class PP(P, Protocol):
        pass

    class PPP(PP, Protocol):
        pass

    class C(DataClass, PPP):
        pass

    assert set(f.name for f in C._fields()) == {"s"}

    class PPNP(PP):
        pass

    class D(DataClass, PPNP):
        pass

    assert set(f.name for f in D._fields()) == {"s"}

    class NP(P):
        pass

    class NPNP(NP):
        pass

    class E(DataClass, NPNP):
        pass

    assert set(f.name for f in D._fields()) == {"s"}

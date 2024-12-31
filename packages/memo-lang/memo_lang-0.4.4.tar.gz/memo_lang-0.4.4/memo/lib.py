import jax
import jax.numpy as jnp
import time
from dataclasses import dataclass

from .core import MemoError

@dataclass
class AuxInfo:
    cost: float | None = None

def marg(t, dims):
    if dims == ():
        return t
    return t.sum(axis=tuple(-1 - d for d in dims), keepdims=True)

def pad(t, total):
    count = total - len(t.shape)
    for _ in range(count):
        t = jnp.expand_dims(t, 0)
    return t

def ffi(f, *args):
    if len(args) == 0:
        return f()
    args = jax.numpy.broadcast_arrays(*args)
    target_shape = args[0].shape
    args = [arg.reshape(-1) for arg in args]
    if isinstance(f, jax.lib.xla_extension.PjitFunction):
        return jax.vmap(f)(*args).reshape(target_shape)
    else:
        raise MemoError(
            f"Tried to call non-JAX function `{f.__name__}`. Use @jax.jit to mark as JAX.",
            hint=f"You tried to call {f}, which is not decorated with @jax.jit.",
            user=True,
            ctxt=None,
            loc=None
        )

def check_domains(tgt, src):  # TODO make this nicer
    if len(tgt) > len(src):
        raise Exception("Not enough arguments to memo call!")
    if len(src) > len(tgt):
        raise Exception("Too many arguments to memo call!")
    for i, (t, s) in enumerate(zip(tgt, src)):
        if t != s:
            raise Exception(f"Domain mismatch in memo call argument {i + 1}: {t} != {s}.")



def pprint_table(f, z):
    def pprint(val):
        if isinstance(val, jnp.ndarray):
            return str(val.item())
        from enum import Enum
        if isinstance(val, Enum):
            return f'{val.name}'
        return str(val)

    rows = []
    rows.append(tuple([f'{ax}: {dom}' for ax, dom in zip(f._axes, f._doms)]) + (f"{f.__name__[5:]}[{', '.join(f._axes)}]",))  # header
    import itertools
    for row in itertools.product(*[enumerate(v) for v in f._vals]):
        idx = tuple([r[0] for r in row])
        lead = tuple([pprint(r[1]) for r in row])
        rows.append(lead + (pprint(z[idx]),))

    widths = []
    for col in range(len(rows[0])):
        widths.append(max([len(row[col]) for row in rows]))

    def hr():
        for w, c in zip(widths, rows[0]):
            print('+', end='-')
            print('-' * w, end='-')
        print('-+')

    hr()
    for ri, row in enumerate(rows):
        for w, c in zip(widths, row):
            print('|', end=' ')
            print(c + ' ' * (w - len(c)), end=' ')
        print(' |')
        if ri == 0:
            hr()
    hr()
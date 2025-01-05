# rust_itertools
Experimental repo to run Rusts itertools in Python.

## Setup
Initially, this will be mostly used as a proof of concept. This is to investigate the comparisons between:
- rust's itertools functionality vs python's itertools functionality
- rust's itertools functionality vs more_itertools functionality
- new rust functions vs more_itertools functionality
- new rust functions vs new python functions around itertools

Practically, this means not all functionality from rust's itertools will be available

## Notes on reasons to use this repository
Often, the major goal of porting Rust functionality over to Python is for speed. So far, my initial experimentation
has shown that that gain is very low (or even non-existant) due to 2 main reasons:
- `itertools` is mostly written in C so already quite fast and roughly on par with Rust
- even for `more_itertools` and new python functions: not having to copy over the results back to Python is a major gain
    vs the rust implementations for the type of functions we deal with here. Example: there are over 36 million
    permutations of the numbers 0 to 9 (incl 9). Generating in Rust and then accessing from Python takes 2.24 seconds
    on my pc, where the CPython itertools takes 0.557 seconds to do the same.

There are some exceptions though, especially for:
- newly written Python code that is not in CPython (both `more_itertools` and additional functions in this repo)
- situations where the Rust compiler can work wonders in reducing logic down to more direct logic
- some tools for which the ratio of compute vs iteration is not as much towards iteration

Next to this, you can use this repository for functionality not available in Python's `itertools` or if you prefer
the way the Rust version is setup.

## Acknowledgements
The Github Actions setup to automatically crossbuild Python packages across operating systems has been based on the
setup in the [rtoml](https://github.com/samuelcolvin/rtoml) project (although first using the old `setuptools` based
setup, because of the link on the `setuptools-rust` page..).

Of course, also credit to the Rust `itertools` [project](https://github.com/rust-itertools/itertools) and inspiration
from the [more-itertools](https://github.com/more-itertools/more-itertools) and of course the core Python itertools
projects.

## Some big ideal TODO's
- Add support for all functionality of any of the `itertools` packages
- Make both a tuple and a list version of each method where applicable
- Make an iterable PyClass (see https://pyo3.rs/v0.22.3/class/protocols#iterable-objects) that can be reused

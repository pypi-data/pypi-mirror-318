use itertools::repeat_n;
use itertools::Itertools;
use pyo3::prelude::*;
use pyo3::pyfunction;
use pyo3::types::PyList;

type T = usize;

#[pyfunction]
fn derangements_range(n: T) -> Vec<Vec<T>> {
    match n {
        2 => vec![vec![1, 0]],
        1 => Vec::new(),
        0 => vec![Vec::new()],
        _ => {
            let mut derangements = Vec::new();
            let lag1 = derangements_range(n - 1);
            for lag in lag1.iter() {
                for split in 0..lag.len() {
                    let mut temp = lag
                        .iter()
                        .enumerate()
                        .map(|x| if x.0 == split { n - 1 } else { *x.1 })
                        .collect_vec();
                    temp.push(lag[split]);
                    derangements.push(temp);
                }
            }

            let lag2 = derangements_range(n - 2);
            for lag in lag2.iter() {
                let mut temp = lag.clone();
                let mut temp2 = lag.clone();
                temp.push(n - 1);
                temp.push(n - 2);
                derangements.push(temp);

                for k in (0..n - 2).rev() {
                    let mut temp = Vec::new();
                    for (i, el) in temp2.iter_mut().enumerate() {
                        if i == k {
                            temp.push(n - 1);
                        }
                        if *el == k {
                            *el = k + 1;
                        }
                        temp.push(*el)
                    }
                    if k == temp2.len() {
                        temp.push(n - 1)
                    }
                    temp.push(k);

                    derangements.push(temp);
                }
            }
            derangements
        }
    }
}

#[pyfunction]
fn permutations(iterable: Bound<PyList>, k: T) -> Vec<Vec<Bound<PyAny>>> {
    iterable.into_iter().permutations(k).collect_vec()
}

#[pyfunction] // TODO not yet Bound<PyList> due to unique() -> needs NewType that implements Clone, Hash and Eq
fn distinct_permutations(iterable: Vec<T>, k: T) -> Vec<Vec<T>> {
    iterable.into_iter().permutations(k).unique().collect_vec()
}

#[pyfunction]
fn derangements(iterable: Vec<T>, k: T) -> Vec<Vec<T>> {
    iterable
        .into_iter()
        .permutations(k)
        .filter(|i| !i.iter().enumerate().any(|x| x.0 == *x.1))
        .collect_vec()
}

#[pyfunction]
fn combinations(iterable: Bound<PyList>, k: T) -> Vec<Vec<Bound<PyAny>>> {
    iterable.into_iter().combinations(k).collect_vec()
}

#[pyfunction]
fn combinations_with_replacement(iterable: Bound<PyList>, k: T) -> Vec<Vec<Bound<PyAny>>> {
    iterable
        .into_iter()
        .combinations_with_replacement(k)
        .collect_vec()
}

#[pyfunction]
fn pairwise(iterable: Bound<PyList>) -> Vec<(Bound<PyAny>, Bound<PyAny>)> {
    iterable.into_iter().tuple_windows().collect()
}

#[pyfunction]
fn repeat(n: Bound<PyAny>, k: T) -> Vec<Bound<PyAny>> {
    repeat_n(n, k).collect_vec()
}

#[pyfunction]
fn powerset(iterable: Bound<PyList>) -> Vec<Vec<Bound<PyAny>>> {
    iterable.into_iter().powerset().collect_vec()
}

const VERSION: &str = env!("CARGO_PKG_VERSION");

#[pymodule]
pub fn _rust_itertools(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("VERSION", VERSION)?;
    m.add_function(wrap_pyfunction!(permutations, m)?)?;
    m.add_function(wrap_pyfunction!(distinct_permutations, m)?)?;
    m.add_function(wrap_pyfunction!(derangements, m)?)?;
    m.add_function(wrap_pyfunction!(combinations, m)?)?;
    m.add_function(wrap_pyfunction!(combinations_with_replacement, m)?)?;
    m.add_function(wrap_pyfunction!(pairwise, m)?)?;
    m.add_function(wrap_pyfunction!(repeat, m)?)?;
    m.add_function(wrap_pyfunction!(powerset, m)?)?;
    m.add_function(wrap_pyfunction!(derangements_range, m)?)?;
    Ok(())
}

#[macro_use]
extern crate derive_builder;

mod payment;
mod activity;
mod test;
mod user;

use pyo3::prelude::*;
use pyo3::types::{PyDict, PyList, PyString};
use crate::activity::Act;
use crate::payment::Payment;



pub fn vkl(_acts: &[Act], ceil: Option<bool>)-> Vec<Payment> {
    let mut acts: Vec<Act> = _acts.iter().map(activity::Act::clone).collect();
    let paid: i64 = acts.iter().map(|act| act.paid).sum();
    let each: i64 = if let Some(ceil_flag) = ceil {
        if ceil_flag {
            (paid as f64 / acts.len() as f64).ceil() as i64
        } else {
            paid / acts.len() as i64
        }
    } else {
        paid / acts.len() as i64
    };

    for act in acts.iter_mut() {
        if act.paid < each {
            act.have_to_pay = each - act.paid;
        } else {
            act.need_to_earn = act.paid - each;
        }
    }

    let (riches, mut pours): (Vec<&mut Act>, Vec<&mut Act>) = acts
        .iter_mut()
        .partition(|act| act.paid > each);

    let mut riches = riches
        .iter()
        .map(|act| activity::Act::clone(act))
        .collect::<Vec<Act>>();

    riches.sort_by(|a, b| b.need_to_earn.cmp(&a.need_to_earn));
    pours.sort_by(|a, b| a.have_to_pay.cmp(&b.have_to_pay));

    let mut payments: Vec<Payment> = Vec::new();

    for rich in riches.iter_mut() {
        for poor in pours.iter_mut() {
            let amount = poor.have_to_pay.min(rich.need_to_earn);
            if amount > 0 {
                let payment = Payment::new(poor.user.clone(), rich.user.clone(), amount);
                payments.push(payment);
            }
            rich.need_to_earn -= amount;
            poor.have_to_pay -= amount;
            if rich.need_to_earn <= 0 {
                break;
            }
        }
    }
    payments
}
fn convert_pyobject_to_acts(py: Python, acts: Vec<PyObject>) -> Vec<Act> {
    let acts: Vec<Act> = acts
        .iter()
        .filter_map(|py_obj| {
            let dict: &PyDict = match py_obj.downcast::<PyDict>(py) {
                Ok(d) => d,
                Err(e) => {
                    eprintln!("Error casting to PyDict: {:?}", e);
                    return None;
                }
            };

            let user = match dict.get_item("user") {
                Ok(Some(user)) => user.to_object(py),
                Ok(None) => {
                    eprintln!("py_dict does not have 'user' key");
                    return None;
                }
                Err(_) => todo!()
            };

            let paid = match dict.get_item("paid") {
                Ok(Some(paid)) => match paid.extract::<i64>() {
                    Ok(val) => val,
                    Err(e) => {
                        eprintln!("Error extracting 'paid' value: {:?}", e);
                        return None;
                    }
                },
                Ok(None) => {
                    eprintln!("py_dict does not have 'paid' key");
                    return None;
                }
                _ => {eprintln!("py_dict does not have 'user' key");
                    return None;}
            };

            Some(Act::new(user, paid))
        })
        .collect();
    acts
}
#[pyfunction]
pub fn calculatee(py: Python, acts: Vec<PyObject>, ceil: Option<bool>) -> PyResult<Vec<Payment>> {
    // pub fn calculate(py: Python, acts: Vec<PyObject>, ceil: Option<bool>) -> Result<String, PyErr>  {

    // let acts = convert_pyobject_to_acts(py, acts);
    // let payments: Vec<Payment> = vkl(&acts, ceil);
    // PytList(payments)
    // let data = serde_json::to_string(&payments).unwrap_or(Err("aaa"));
    // Ok(data)
    // let data = serde_json::to_string(&payments).unwrap();
    // Ok(data)
    todo!()
}


#[pyfunction]
pub fn calculate(py: Python, acts: Vec<PyObject>, ceil: Option<bool>) -> PyResult<&PyList> {
    let acts = convert_pyobject_to_acts(py, acts);
    let payments: Vec<Payment> = vkl(&acts, ceil);
    let d: Vec<PyObject> = payments.iter().map(|payment| payment.to_dict(py)).collect();
    let list = PyList::new(py, d);
    Ok(list)
}


#[pyfunction]
fn sum_as_string(py: Python<'_>, a: i32, b: i32) -> PyResult<&PyAny>  {
    let result = a + b;
    let py_future = pyo3_asyncio::tokio::future_into_py(py, async move {
        // Create the result string
        let result_string = result.to_string();
        // Acquire the GIL and create a PyString
        Python::with_gil(|py| {
            Ok(PyString::new(py, &result_string).to_object(py))
        })
    })?;
    Ok(py_future)
}

#[pyfunction]
fn rust_sleep(py: Python<'_>) -> PyResult<&PyAny> {
    pyo3_asyncio::tokio::future_into_py(py, async {
        Ok(Python::with_gil(|py| py.None()))
    })
}


/// A Python module implemented in Rust.
#[pymodule]
#[allow(unused_variables)]
fn teammate_cores(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Payment>()?;
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(calculate, m)?)?;
    m.add_function(wrap_pyfunction!(rust_sleep, m)?)?;
    Ok(())
}

use pyo3::prelude::*;
use derive_builder::Builder;


#[pyclass]
#[derive(Debug, Clone, Builder)]
pub struct Act {
    pub user: PyObject,
    pub paid: i64,

    #[builder(default="0")]
    pub have_to_pay: i64,

    #[builder(default = "0")]
    pub need_to_earn: i64,
}


#[pymethods]
impl Act {
    #[new]
    pub fn new(user: PyObject, paid: i64) -> Self {
        Act {
            user,
            paid,
            have_to_pay: 0,
            need_to_earn: 0,
        }
    }
}

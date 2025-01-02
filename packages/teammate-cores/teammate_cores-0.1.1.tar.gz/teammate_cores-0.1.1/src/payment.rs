use pyo3::{pyclass, pymethods, PyObject, Python};
use pyo3::types::PyDict;
#[pyclass]
#[derive(Debug, Clone)]
pub struct Payment {
    pub src: PyObject,
    pub dst: PyObject,
    pub amount: i64,
}

#[pymethods]
impl Payment {
    #[new]
    pub fn new(src: PyObject, dst: PyObject, amount: i64) -> Self {
        Payment { src, dst, amount }
    }

    pub fn to_dict(&self, py: Python) -> PyObject {
        let dict = PyDict::new(py);
        dict.set_item("src", &self.src).unwrap();
        dict.set_item("dst", &self.dst).unwrap();
        dict.set_item("amount", self.amount).unwrap();
        dict.into()
    }
}

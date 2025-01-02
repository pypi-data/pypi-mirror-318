use pyo3::{Py, PyAny, pyclass, Python, ToPyObject};
use pyo3::types::PyString;
use serde::{Deserialize, Deserializer, Serialize, Serializer};

#[pyclass]
#[derive(Debug, Clone)]
pub struct PyUser {
    pub user: Py<PyAny>
}


// Implement custom serialization for PyUser
impl Serialize for PyUser {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        // Serialize the Python object as a string representation
        Python::with_gil(|py| {
            let user_str = self.user.as_ref(py).str().map_err(serde::ser::Error::custom)?.to_str().map_err(serde::ser::Error::custom)?;
            serializer.serialize_str(user_str)
        })
    }
}

impl<'de> Deserialize<'de> for PyUser {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        let user_str = String::deserialize(deserializer)?;
        Python::with_gil(|py| {
            let user = PyString::new(py, &user_str).to_object(py);
            Ok(PyUser { user: user.into() })
        })
    }
}

pub mod accuracy;
pub mod activation;
pub mod dyn_layer;
pub mod layer;
pub mod loss;
pub mod model;
pub mod optimizer;
pub mod sample_data;
pub mod pyo3_bindings;

use pyo3::prelude::*;

#[pymodule]
fn nno3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::create_linear_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::create_categorical_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::add_linear_model_layer, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::add_categorical_model_layer, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::create_optimizer, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::train_linear_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::train_categorical_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::load_linear_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::evaluate_linear_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::load_categorical_model, m)?)?;
    m.add_function(wrap_pyfunction!(crate::pyo3_bindings::bindings::evaluate_categorical_model, m)?)?;
    Ok(())
}

#[cfg(test)]
pub mod tests;

/// Alias for [`std::result::Result`] that wraps our [Error] type.
pub type Result<T> = std::result::Result<T, Error>;

/// Error type for this crate.
#[derive(thiserror::Error, Debug)]
pub enum Error {
    #[error(transparent)]
    Python(#[from] pyo3::PyErr),
}

/// Convert [Error] to [`pyo3::PyErr`].
impl From<Error> for pyo3::PyErr {
    fn from(e: Error) -> Self {
        match e {
            Error::Python(e) => e,
            // _ => pyo3::exceptions::PyException::new_err(e.to_string()),
        }
    }
}

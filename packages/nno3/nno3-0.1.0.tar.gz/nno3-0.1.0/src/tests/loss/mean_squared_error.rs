use ndarray::array;
use crate::loss::mean_squared_error;

#[test]
fn loss_mean_absolute_error_backward() {
    let dvalues = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y_true = array![1.0, 1.0, 5.0];
    let out = mean_squared_error::backward(&dvalues, &y_true);
    assert_eq!(
        out,
        array![[-0.0, 0.33333334], [0.6666667, 1.0], [-0.0, 0.33333334]]
    );
}

#[test]
fn loss_mean_absolute_error_calculate() {
    let predictions = array![1.0, 2.0, 3.0, 4.0, 5.0];
    let y = array![1.0, 2.0, 3.0, 3.0, 3.0];
    let data_loss = mean_squared_error::calculate(&predictions, &y);
    assert_eq!(data_loss, 1.0);
}

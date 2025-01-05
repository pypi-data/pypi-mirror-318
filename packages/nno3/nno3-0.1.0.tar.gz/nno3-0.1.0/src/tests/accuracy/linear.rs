use ndarray::array;
use crate::accuracy::linear;

#[test]
fn linear_calculate() {
    let predictions = array![1.0, 2.0, 3.0, 4.0, 5.0];
    let y = array![1.0, 1.0, 3.0, 4.0, 5.0];
    assert_eq!(linear::calculate(&predictions, &y, 0.5), 0.8);
    assert_eq!(linear::calculate(&predictions, &y, 1.0), 1.0);
}

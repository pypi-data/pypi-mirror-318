use ndarray::array;
use crate::activation::relu;
use crate::layer::dense;

#[test]
fn activation_relu_forward() {
    let inputs = array![[-0.1, -0.2], [0.3, 0.4], [0.5, -0.6]];
    let weights = array![[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]];
    let biases = array![-0.1, -0.2, 0.3];
    let output = dense::forward(&inputs, &weights, &biases);
    assert_eq!(
        relu::forward(&output),
        array![
            [0.0, 0.0, 0.15],
            [0.09000001, 0.059999987, 0.63],
            [0.0, 0.0, 0.08999999]
        ]
    );
}

#[test]
fn activation_relu_backward() {
    let inputs = array![[-0.1, -0.2], [0.3, 0.4], [0.5, -0.6]];
    let output = array![[0.1, -0.2], [0.3, 0.4], [0.5, 0.6]];
    assert_eq!(
        relu::backward(&inputs, &output),
        array![[0.0, 0.0], [0.3, 0.4], [0.5, 0.0]]
    );
}

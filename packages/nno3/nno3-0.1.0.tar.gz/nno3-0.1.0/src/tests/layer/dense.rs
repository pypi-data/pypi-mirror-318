use ndarray::array;
use crate::dyn_layer::Layer;
use crate::layer::dense;

#[test]
fn layer_dense_forward() {
    let inputs = array![[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]];
    let weights = array![[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]];
    let biases = array![0.1, 0.2, 0.3];
    assert_eq!(
        dense::forward(&inputs, &weights, &biases),
        array![
            [0.19, 0.32, 0.45000002],
            [0.29000002, 0.45999998, 0.63],
            [0.39000002, 0.6, 0.81000006]
        ]
    );
}

#[test]
fn layer_dense_backward() {
    let mut cell = Layer {
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    cell.weights = array![[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]];
    cell.biases = array![-0.1, -0.2, 0.3];
    let inputs = array![[-0.1, -0.2], [0.3, 0.4], [0.5, -0.6]];
    let mut output = cell.forward(&inputs, true);
    assert_eq!(
        dense::backward(&mut cell, &mut output),
        array![
            [0.045, 0.09],
            [0.21000001, 0.444],
            [0.026999997, 0.053999994]
        ]
    );
    assert_eq!(
        cell.dweights,
        array![
            [0.027000004, 0.017999997, 0.21900001],
            [0.036000006, 0.023999995, 0.16800001]
        ]
    );
    assert_eq!(cell.dbiases, array![0.09000001, 0.059999987, 0.86999995]);
}

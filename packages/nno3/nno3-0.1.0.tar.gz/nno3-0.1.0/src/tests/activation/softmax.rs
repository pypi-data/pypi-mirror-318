use ndarray::array;
use crate::activation::softmax;

#[test]
fn softmax_forward() {
    let inputs = array![[0.9, 0.5, 0.1], [0.1, 0.9, 0.5], [0.1, 0.5, 0.9]];
    assert_eq!(
        softmax::forward(&inputs),
        array![
            [0.47177625, 0.31624106, 0.21198274],
            [0.21198274, 0.47177625, 0.31624106],
            [0.21198274, 0.31624106, 0.47177625]
        ]
    );
    let inputs = array![[-0.1, -0.5, -0.9], [-0.9, -0.1, -0.5], [-0.5, -0.1, -0.9]];
    assert_eq!(
        softmax::forward(&inputs),
        array![
            [0.47177625, 0.31624106, 0.21198274],
            [0.21198274, 0.47177625, 0.31624106],
            [0.31624106, 0.47177625, 0.21198274]
        ]
    );
}

#[test]
fn softmax_predict() {
    let inputs = array![
        [0.0009, 0.0005, 0.0001],
        [0.0001, 0.0009, 0.0005],
        [0.0001, 0.0005, 0.0009]
    ];
    let outputs = softmax::forward(&inputs);
    assert_eq!(softmax::predict(&outputs), vec![0, 1, 2]);
}

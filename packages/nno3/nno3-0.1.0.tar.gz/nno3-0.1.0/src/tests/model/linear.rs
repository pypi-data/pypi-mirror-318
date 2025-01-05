use ndarray::array;
use crate::dyn_layer::Layer;
use crate::model::linear::LinearModel;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;
use crate::sample_data;
use std::fs::File;

#[test]
fn linear_model_forward() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = LinearModel {
        layers,
        output_type: "linear".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    assert_eq!(output.shape(), &[3, 2]);
    assert!(output.mean().unwrap() >= 0.0);
}

#[test]
fn linear_model_predict() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = LinearModel {
        layers,
        output_type: "linear".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    let predictions = model.predict(&output);
    assert_eq!(predictions.shape(), &[3]);
    assert!(predictions.mean().unwrap() >= 0.0);
}

#[test]
fn linear_model_loss() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y = array![1.0, 3.0, 5.0];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = LinearModel {
        layers,
        output_type: "linear".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    let predictions = model.predict(&output);
    assert!(11.0 <= model.data_loss(&predictions, &y) && model.data_loss(&predictions, &y) <= 12.0);
    model.layers[0].biases = array![2.0, 0.0, 0.0];
    model.layers[0].bias_regularizer_l1 = 1.0;
    assert!(2.0 < model.regularization_loss() && model.regularization_loss() < 3.0);
    model.layers[0].bias_regularizer_l1 = 0.0;
    model.layers[0].bias_regularizer_l2 = 1.0;
    assert!(4.0 < model.regularization_loss() && model.regularization_loss() < 5.0);
    model.layers[0].bias_regularizer_l2 = 0.0;
    model.layers[0].weight_regularizer_l1 = 1.0;
    assert!(0.0 < model.regularization_loss() && model.regularization_loss() < 1.0);
    model.layers[0].weight_regularizer_l1 = 0.0;
    model.layers[0].weight_regularizer_l2 = 1.0;
    assert!(0.0 < model.regularization_loss() && model.regularization_loss() < 1.0);
}

#[test]
fn linear_model_accuracy() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y = array![1.0, 3.0, 5.0];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = LinearModel {
        layers,
        output_type: "linear".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    let predictions = model.predict(&output);
    assert!(0.0 <= model.accurary(&predictions, &y) && model.accurary(&predictions, &y) <= 1.0);
}

#[test]
fn linear_model_backward() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y = array![1.0, 3.0, 5.0];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = LinearModel {
        layers,
        output_type: "linear".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    model.backward(output, &y);
    assert_eq!(model.layers[0].dweights.shape(), &[2, 8]);
    assert_eq!(model.layers[0].dbiases.shape(), &[8]);
    assert!(
        -1.0 < model.layers[0].dweights.mean().unwrap()
            && model.layers[0].dweights.mean().unwrap() < 1.0
    );
    assert!(
        -1.0 < model.layers[0].dbiases.mean().unwrap()
            && model.layers[0].dbiases.mean().unwrap() < 1.0
    );
}

#[test]
fn correct_model_output_shape() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y = array![1.0, 3.0, 5.0];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: y.shape().len(),
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = LinearModel {
        layers,
        output_type: "linear".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    let preds = model.predict(&output);
    for i in 0..output.shape()[0] {
        assert_eq!(output.row(i).shape(), &[1]);
        assert_eq!(output.row(i)[0], preds[i]);
    }
}

#[test]
fn linear_preprocess() {
    let mut x = array![[2.2, 3.3, 4.4], [10.0, 12.0, 14.0]];
    LinearModel::preprocess(&mut x);
    assert_eq!(
        x,
        array![[0.0, 0.09322033, 0.18644068], [0.66101694, 0.8305085, 1.0]]
    );
    let mut x = array![[-2.2, 3.3, 4.4], [10.0, 12.0, -14.0]];
    LinearModel::preprocess(&mut x);
    assert_eq!(
        x,
        array![[0.45384616, 0.6653846, 0.70769227], [0.9230769, 1.0, 0.0]]
    );
}

#[test]
fn linear_model_nnfs_validation() {
    let x = array![
        [11.753203, 51.793568, 51.818596,],
        [11.917669, 82.2479, 34.519077,],
        [29.804298, 71.38458, 27.292387,],
        [68.53252, 79.63844, 73.669525,],
        [38.913723, 30.119867, 15.946266,],
        [35.465717, 23.2893, 6.646216,],
        [98.379616, 2.977749, 73.04323,],
        [79.96565, 49.926468, 26.412313,],
        [90.82938, 21.684448, 93.26243,],
        [0.53967345, 86.115395, 48.804306,]
    ];
    let y = array![
        115.365367,
        128.684646,
        128.481265,
        221.840485,
        84.979856,
        65.401233,
        174.400595,
        156.304431,
        205.776258,
        135.45937445
    ];
    let mut layer1 = Layer {
        layer_type: "dense".to_owned(),
        n_inputs: 3,
        n_neurons: 8,
        ..Default::default()
    };
    layer1.init();
    let mut layer2 = Layer {
        layer_type: "dense".to_owned(),
        n_inputs: 8,
        n_neurons: 1,
        ..Default::default()
    };
    layer2.init();
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        learning_rate: 0.001,
        decay: 0.01,
        ..Default::default()
    };
    opt.init();
    layer1.weights = array![
        [-0.01, 0.01, -0.01, 0.01, -0.01, 0.01, -0.01, 0.01],
        [-0.01, 0.01, -0.01, 0.01, -0.01, 0.01, -0.01, 0.01],
        [-0.01, 0.01, -0.01, 0.01, -0.01, 0.01, -0.01, 0.01]
    ];
    layer2.weights = array![
        [-0.01],
        [0.01],
        [-0.01],
        [0.01],
        [-0.01],
        [0.01],
        [-0.01],
        [0.01]
    ];
    // forward pass
    let output1 = layer1.forward(&x, true);
    assert_eq!(
        output1.to_owned(),
        array![
            [
                -1.1536536, 1.1536536, -1.1536536, 1.1536536, -1.1536536, 1.1536536, -1.1536536,
                1.1536536
            ],
            [
                -1.2868465, 1.2868465, -1.2868465, 1.2868465, -1.2868465, 1.2868465, -1.2868465,
                1.2868465
            ],
            [
                -1.2848126, 1.2848126, -1.2848126, 1.2848126, -1.2848126, 1.2848126, -1.2848126,
                1.2848126
            ],
            [
                -2.2184048, 2.2184048, -2.2184048, 2.2184048, -2.2184048, 2.2184048, -2.2184048,
                2.2184048
            ],
            [
                -0.8497985, 0.8497985, -0.8497985, 0.8497985, -0.8497985, 0.8497985, -0.8497985,
                0.8497985
            ],
            [
                -0.6540123, 0.6540123, -0.6540123, 0.6540123, -0.6540123, 0.6540123, -0.6540123,
                0.6540123
            ],
            [
                -1.7440059, 1.7440059, -1.7440059, 1.7440059, -1.7440059, 1.7440059, -1.7440059,
                1.7440059
            ],
            [
                -1.5630443, 1.5630443, -1.5630443, 1.5630443, -1.5630443, 1.5630443, -1.5630443,
                1.5630443
            ],
            [
                -2.0577624, 2.0577624, -2.0577624, 2.0577624, -2.0577624, 2.0577624, -2.0577624,
                2.0577624
            ],
            [
                -1.3545938, 1.3545938, -1.3545938, 1.3545938, -1.3545938, 1.3545938, -1.3545938,
                1.3545938
            ]
        ]
    );
    let output = crate::activation::relu::forward(&output1);
    assert_eq!(
        output.to_owned(),
        array![
            [0.0, 1.1536536, 0.0, 1.1536536, 0.0, 1.1536536, 0.0, 1.1536536],
            [0.0, 1.2868465, 0.0, 1.2868465, 0.0, 1.2868465, 0.0, 1.2868465],
            [0.0, 1.2848126, 0.0, 1.2848126, 0.0, 1.2848126, 0.0, 1.2848126],
            [0.0, 2.2184048, 0.0, 2.2184048, 0.0, 2.2184048, 0.0, 2.2184048],
            [0.0, 0.8497985, 0.0, 0.8497985, 0.0, 0.8497985, 0.0, 0.8497985],
            [0.0, 0.6540123, 0.0, 0.6540123, 0.0, 0.6540123, 0.0, 0.6540123],
            [0.0, 1.7440059, 0.0, 1.7440059, 0.0, 1.7440059, 0.0, 1.7440059],
            [0.0, 1.5630443, 0.0, 1.5630443, 0.0, 1.5630443, 0.0, 1.5630443],
            [0.0, 2.0577624, 0.0, 2.0577624, 0.0, 2.0577624, 0.0, 2.0577624],
            [0.0, 1.3545938, 0.0, 1.3545938, 0.0, 1.3545938, 0.0, 1.3545938]
        ]
    );
    let output = layer2.forward(&output, true);
    assert_eq!(
        output.to_owned(),
        array![
            [0.046146143],
            [0.05147386],
            [0.0513925],
            [0.088736184],
            [0.03399194],
            [0.026160492],
            [0.06976023],
            [0.06252177],
            [0.08231049],
            [0.054183748]
        ]
    );
    let output = crate::activation::linear::forward(&output);
    assert_eq!(
        output.to_owned(),
        array![
            [0.046146143],
            [0.05147386],
            [0.0513925],
            [0.088736184],
            [0.03399194],
            [0.026160492],
            [0.06976023],
            [0.06252177],
            [0.08231049],
            [0.054183748]
        ]
    );
    let predictions = crate::activation::linear::predict(&output);
    let loss = crate::loss::mean_squared_error::calculate(&predictions, &y);
    assert_eq!(loss.to_owned(), 22245.012);

    // backward pass
    let dvalues = crate::loss::mean_squared_error::backward(&output, &y);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [-23.063845],
            [-25.726635],
            [-25.685974],
            [-44.35035],
            [-16.989174],
            [-13.075014],
            [-34.866165],
            [-31.248383],
            [-41.13879],
            [-27.08104]
        ]
    );
    let dvalues = crate::activation::linear::backward(&dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [-23.063845],
            [-25.726635],
            [-25.685974],
            [-44.35035],
            [-16.989174],
            [-13.075014],
            [-34.866165],
            [-31.248383],
            [-41.13879],
            [-27.08104]
        ]
    );
    let dvalues = layer2.backward(&dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [
                0.23063844,
                -0.23063844,
                0.23063844,
                -0.23063844,
                0.23063844,
                -0.23063844,
                0.23063844,
                -0.23063844
            ],
            [
                0.25726634,
                -0.25726634,
                0.25726634,
                -0.25726634,
                0.25726634,
                -0.25726634,
                0.25726634,
                -0.25726634
            ],
            [
                0.25685975,
                -0.25685975,
                0.25685975,
                -0.25685975,
                0.25685975,
                -0.25685975,
                0.25685975,
                -0.25685975
            ],
            [
                0.4435035, -0.4435035, 0.4435035, -0.4435035, 0.4435035, -0.4435035, 0.4435035,
                -0.4435035
            ],
            [
                0.16989173,
                -0.16989173,
                0.16989173,
                -0.16989173,
                0.16989173,
                -0.16989173,
                0.16989173,
                -0.16989173
            ],
            [
                0.13075013,
                -0.13075013,
                0.13075013,
                -0.13075013,
                0.13075013,
                -0.13075013,
                0.13075013,
                -0.13075013
            ],
            [
                0.34866163,
                -0.34866163,
                0.34866163,
                -0.34866163,
                0.34866163,
                -0.34866163,
                0.34866163,
                -0.34866163
            ],
            [
                0.31248382,
                -0.31248382,
                0.31248382,
                -0.31248382,
                0.31248382,
                -0.31248382,
                0.31248382,
                -0.31248382
            ],
            [
                0.4113879, -0.4113879, 0.4113879, -0.4113879, 0.4113879, -0.4113879, 0.4113879,
                -0.4113879
            ],
            [
                0.2708104, -0.2708104, 0.2708104, -0.2708104, 0.2708104, -0.2708104, 0.2708104,
                -0.2708104
            ]
        ]
    );
    let dvalues = crate::activation::relu::backward(&output1, &dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [
                0.0,
                -0.23063844,
                0.0,
                -0.23063844,
                0.0,
                -0.23063844,
                0.0,
                -0.23063844
            ],
            [
                0.0,
                -0.25726634,
                0.0,
                -0.25726634,
                0.0,
                -0.25726634,
                0.0,
                -0.25726634
            ],
            [
                0.0,
                -0.25685975,
                0.0,
                -0.25685975,
                0.0,
                -0.25685975,
                0.0,
                -0.25685975
            ],
            [0.0, -0.4435035, 0.0, -0.4435035, 0.0, -0.4435035, 0.0, -0.4435035],
            [
                0.0,
                -0.16989173,
                0.0,
                -0.16989173,
                0.0,
                -0.16989173,
                0.0,
                -0.16989173
            ],
            [
                0.0,
                -0.13075013,
                0.0,
                -0.13075013,
                0.0,
                -0.13075013,
                0.0,
                -0.13075013
            ],
            [
                0.0,
                -0.34866163,
                0.0,
                -0.34866163,
                0.0,
                -0.34866163,
                0.0,
                -0.34866163
            ],
            [
                0.0,
                -0.31248382,
                0.0,
                -0.31248382,
                0.0,
                -0.31248382,
                0.0,
                -0.31248382
            ],
            [0.0, -0.4113879, 0.0, -0.4113879, 0.0, -0.4113879, 0.0, -0.4113879],
            [0.0, -0.2708104, 0.0, -0.2708104, 0.0, -0.2708104, 0.0, -0.2708104]
        ]
    );
    let dvalues = layer1.backward(&dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [-0.009225538, -0.009225538, -0.009225538],
            [-0.010290653, -0.010290653, -0.010290653],
            [-0.01027439, -0.01027439, -0.01027439],
            [-0.01774014, -0.01774014, -0.01774014],
            [-0.006795669, -0.006795669, -0.006795669],
            [-0.0052300054, -0.0052300054, -0.0052300054],
            [-0.013946465, -0.013946465, -0.013946465],
            [-0.012499352, -0.012499352, -0.012499352],
            [-0.016455514, -0.016455514, -0.016455514],
            [-0.010832415, -0.010832415, -0.010832415]
        ]
    );

    // update params
    opt.pre_update_params();
    opt.update_params(&mut layer1);
    assert_eq!(
        layer1.weights.to_owned(),
        array![
            [-0.01, 0.011, -0.01, 0.011, -0.01, 0.011, -0.01, 0.011],
            [-0.01, 0.011, -0.01, 0.011, -0.01, 0.011, -0.01, 0.011],
            [-0.01, 0.011, -0.01, 0.011, -0.01, 0.011, -0.01, 0.011]
        ]
    );
    assert_eq!(
        layer1.biases.to_owned(),
        array![0.0, 0.001, 0.0, 0.001, 0.0, 0.001, 0.0, 0.001]
    );
    opt.update_params(&mut layer2);
    assert_eq!(
        layer2.weights.to_owned(),
        array![
            [-0.01],
            [0.011],
            [-0.01],
            [0.011],
            [-0.01],
            [0.011],
            [-0.01],
            [0.011]
        ]
    );
    assert_eq!(layer2.biases.to_owned(), array![0.001]);
    opt.post_update_params();

    for _ in 0..98 {
        let output1 = layer1.forward(&x, true);
        let output = crate::activation::relu::forward(&output1);
        let output = layer2.forward(&output, true);
        let output = crate::activation::linear::forward(&output);

        let dvalues = crate::loss::mean_squared_error::backward(&output, &y);
        let dvalues = layer2.backward(&dvalues);
        let dvalues = crate::activation::relu::backward(&output1, &dvalues);
        let _ = layer1.backward(&dvalues);

        opt.pre_update_params();
        opt.update_params(&mut layer1);
        opt.update_params(&mut layer2);
        opt.post_update_params();
    }

    let output = layer1.forward(&x, true);
    let output = crate::activation::relu::forward(&output);
    let output = layer2.forward(&output, true);
    let output = crate::activation::linear::forward(&output);
    assert_eq!(
        output.to_owned(),
        array![
            [4.386947],
            [4.88165],
            [4.8740983],
            [8.341684],
            [3.2583597],
            [2.531164],
            [6.5796695],
            [5.9075227],
            [7.7450337],
            [5.1332793]
        ]
    );
}

#[test]
fn linear_model_performance() {
    let (x, y) = sample_data::create_linear_data(1000, 5);
    let (val_x, val_y) = sample_data::create_linear_data(10, 5);
    let hidden_layer_size = 64;
    let save_best_params = "model_backup/linear_model_best_weights.json";
    let mut model = LinearModel {
        output_type: "linear".to_owned(),
        save_best_params: save_best_params.to_owned(),
        acc_precision: 1.0,
        ..Default::default()
    };
    model.layers.push(Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    });
    model.layers.push(Layer {
        n_inputs: hidden_layer_size,
        n_neurons: y.shape().len(),
        layer_type: "dense".to_owned(),
        ..Default::default()
    });
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        learning_rate: 0.001,
        decay: 0.01,
        ..Default::default()
    };
    model.finalize(&mut opt);
    let num_epochs = 1000;
    let print_every = num_epochs / 10;
    model.train(
        num_epochs,
        print_every,
        x,
        &y,
        val_x.to_owned(),
        &val_y,
        opt,
    );

    let load = File::open(save_best_params.to_owned()).unwrap();
    let mut load_model: LinearModel = serde_json::from_reader(load).unwrap();
    load_model.test(val_x, val_y);
}

use ndarray::{Array1, Array2};
use ndarray_rand::rand::{self, Rng};

pub fn create_vote_data(n_samples: usize, n_classes: usize) -> (Array2<f32>, Vec<i32>) {
    let mut x_out: Array2<f32> = Array2::zeros((n_samples, n_classes));
    x_out.iter_mut().for_each(|val| {
        let rand: f32 = rand::thread_rng().gen();
        *val = rand * 100.0;
    });
    let mut y_out = vec![0; n_samples];
    for row in 0..x_out.shape()[0] {
        let mut max_value = 0.0;
        for col in 0..x_out.shape()[1] {
            if col == 0 {
                y_out[row] = col as i32;
                max_value = x_out[[row, col]];
            } else {
                if x_out[[row, col]] > max_value {
                    y_out[row] = col as i32;
                    max_value = x_out[[row, col]];
                }
            }
        }
    }
    return (x_out, y_out);
}

pub fn create_linear_data(n_samples: usize, n_classes: usize) -> (Array2<f32>, Array1<f32>) {
    let mut x_out: Array2<f32> = Array2::zeros((n_samples, n_classes));
    x_out.iter_mut().for_each(|val| {
        let rand: f32 = rand::thread_rng().gen();
        *val = rand * 100.0;
    });
    let mut y_out: Array1<f32> = Array1::zeros(n_samples);
    y_out
        .iter_mut()
        .enumerate()
        .for_each(|(i, val)| *val = x_out.row(i).sum());
    return (x_out, y_out);
}

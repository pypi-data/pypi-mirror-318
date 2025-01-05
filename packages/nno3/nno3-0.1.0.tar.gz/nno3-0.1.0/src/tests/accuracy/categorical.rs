use crate::accuracy::categorical;

#[test]
fn categorical_calculate() {
    let predictions = vec![1, 2, 3, 4];
    let y = vec![1, 1, 3, 4];
    assert_eq!(categorical::calculate(&predictions, &y), 0.75);
}

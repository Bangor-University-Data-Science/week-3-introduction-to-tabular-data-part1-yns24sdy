from titanic_analysis.feature_type_dict import create_feature_type_dict
import pandas as pd

def test_create_feature_type_dict():
    mock_df = pd.DataFrame({
        'Age': [22, 38, 26, 35],
        'Sex': ['male', 'female', 'female', 'male'],
        'Survived': [0, 1, 1, 0]
    })
    feature_types = create_feature_type_dict(mock_df)
    expected_types = {'numerical_continuous', 'categorical_ordinal'}
    assert set(feature_types.values()) & expected_types == expected_types

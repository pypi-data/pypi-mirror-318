import os
import numpy as np

def load_inputs_target_pairs(inputs_channels: dict, target_channels: dict, static_channels: dict = None, data_path: str = None, as_dict=False):
    
    def check_shape_consistency(data_dict):
        shapes = [arr.shape for arr in data_dict.values()]
        if not all(shape == shapes[0] for shape in shapes):
            raise ValueError(f"Inconsistent shapes found: {shapes}")
    
    # Load input channels
    sel_inputs_channels = {}
    for channel, npy_path in inputs_channels.items():
        npy_full_path = npy_path if os.path.isabs(npy_path) else os.path.join(data_path, npy_path)
        print(f'\nLoading Inputs Channel ... {channel}: {npy_full_path}')
        sel_inputs_channels[channel] = np.load(npy_full_path)
        print(f'\tShape: {sel_inputs_channels[channel].shape}')
    
    # Check consistency and stack inputs
    check_shape_consistency(sel_inputs_channels)
    inputs = np.stack(list(sel_inputs_channels.values()), axis=3)

    print(f"\n\tFinished Processing Inputs Channels: {inputs.shape}")
    print('*'*100)
    
    # Load target channels
    sel_target_channels = {}
    for channel, npy_path in target_channels.items():
        npy_full_path = npy_path if os.path.isabs(npy_path) else os.path.join(data_path, npy_path)
        print(f'\nLoading Target Channel ... {channel}: {npy_full_path}')
        sel_target_channels[channel] = np.load(npy_full_path)
        print(f'\tShape: {sel_target_channels[channel].shape}')
    
    # Check consistency and stack targets
    check_shape_consistency(sel_target_channels)
    target = np.stack(list(sel_target_channels.values()), axis=3)

    print(f"\n\tFinished Processing Target Channels: {target.shape}")
    print('*'*100)
    
    if static_channels is not None:
        # Load static channels
        sel_static_channels = {}
        for channel, npy_path in static_channels.items():
            npy_full_path = npy_path if os.path.isabs(npy_path) else os.path.join(data_path, npy_path)
            print(f'\nLoading Static Channel ... {channel}: {npy_full_path}')
            sel_static_channels[channel] = np.load(npy_full_path)
            print(f'\tShape: {sel_static_channels[channel].shape}')
        
        # Check consistency and stack static channels
        check_shape_consistency(sel_static_channels)
        static = np.stack(list(sel_static_channels.values()), axis=3)

        print(f"\n\tFinished Processing Static Channels: {static.shape}")
        print('*'*100)
        
        result = {'inputs': inputs, 'static': static, 'target': target}
    else:
        result = {'inputs': inputs, 'target': target}
    
    return result if as_dict else tuple(result.values())

def take_paired_data_subset_by_bounds(X, y, S=None, bounds=(None, None)):
    """
    Splits data into training, validation, and test sets based on index bounds.
    Ensures that the first axis length of X and y match.
    
    Parameters:
    - X: Input features array (e.g., NumPy array, tensor, etc.)
    - y: Target array
    - S: Optional secondary input features array
    - bounds: Tuple specifying the start and end index for subsetting (inclusive, exclusive)
    
    Returns:
    - A tuple of the subsets based on the provided bounds.
    
    Raises:
    - ValueError: If the first axis of X and y are not the same length.
    """
    # Validate that the first axis lengths of X and y are the same
    if X.shape[0] != y.shape[0]:
        raise ValueError(f"The first axis lengths of X and y must match. "
                         f"Got X.shape[0] = {X.shape[0]}, y.shape[0] = {y.shape[0]}")

    # # Print the shape of data before subsetting
    # print(f"Data before subsetting:")
    # print(f"X shape: {X.shape}, y shape: {y.shape}")
    if S is not None:
        print(f"S shape: {S.shape}")

    # Subset the data
    X_subset = X[bounds[0]:bounds[1]]
    y_subset = y[bounds[0]:bounds[1]]
    S_subset = S[bounds[0]:bounds[1]] if S is not None else None

    # # Print the shape of data after subsetting
    # print(f"Data after subsetting:")
    # print(f"X_subset shape: {X_subset.shape}, y_subset shape: {y_subset.shape}")
    if S_subset is not None:
        print(f"S_subset shape: {S_subset.shape}")

    # Return the subsets
    if S is not None:
        return X_subset, S_subset, y_subset
    else:
        return X_subset, y_subset

def train_val_split_by_bounds(X, y, S=None,
                              train_bounds=(0, 9308), val_bounds=(9308, 11098), test_bounds=(11098, -1),
                              test_only=False,
                             ):
    """
    Splits data into training, validation, and test sets based on index bounds.
    """
    # Extract test data only
    if test_only:
        if S is not None:
            return (
                X[test_bounds[0]:test_bounds[1]],
                S[test_bounds[0]:test_bounds[1]],
                y[test_bounds[0]:test_bounds[1]]
            )
        else:
            return (
                X[test_bounds[0]:test_bounds[1]],
                y[test_bounds[0]:test_bounds[1]]
            )

    # Extract train and validation data
    if S is not None:
        return (
            X[train_bounds[0]:train_bounds[1]], X[val_bounds[0]:val_bounds[1]],
            S[train_bounds[0]:train_bounds[1]], S[val_bounds[0]:val_bounds[1]],
            y[train_bounds[0]:train_bounds[1]], y[val_bounds[0]:val_bounds[1]]
        )
    else:
        return (
            X[train_bounds[0]:train_bounds[1]], X[val_bounds[0]:val_bounds[1]],
            y[train_bounds[0]:train_bounds[1]], y[val_bounds[0]:val_bounds[1]]
        )

def train_val_split(X, y, S=None, train_bounds=None, val_bounds=None, test_only=False, test_bounds=12784):
    if train_bounds is None:
        train_bounds = np.concatenate([
            np.arange(366, 1827),
            np.arange(2192, 3653),
            np.arange(4018, 5479),
            np.arange(5844, 7305),
            np.arange(7671, 9132),
            np.arange(9497, 10598),
            np.arange(11322, 12784)
        ])
    
    if val_bounds is None:
        val_bounds = np.concatenate([
            np.arange(0, 366),
            np.arange(1827, 2192),
            np.arange(3653, 4018),
            np.arange(5479, 5844),
            np.arange(7305, 7671),
            np.arange(9132, 9497),
            np.arange(10598, 11322)
        ])
    
    if S is not None:
        
        if test_only:
            return X[test_bounds:], S[test_bounds:], y[test_bounds:] 
        
        else:
            return X[train_bounds], X[val_bounds], S[train_bounds], S[val_bounds], y[train_bounds], y[val_bounds]
    
    else:
        
        if test_only:
            return X[test_bounds:], y[test_bounds:] 

        else:
            return X[train_bounds], X[val_bounds], y[train_bounds], y[val_bounds]
        
def fetch_inputs_target_pairs(inputs_channels: dict, target_channels: dict, static_channels: dict = None, data_path: str = None, as_dict=False):
    
    # Select Inputs Channels
    sel_inputs_channels = {}
    for channel, npy_path in inputs_channels.items():
        npy_full_path = npy_path if data_path is None else f'{data_path}/{npy_path}'
        print(f'\tLoading Inputs Channel ... {channel}: {npy_full_path}')
        sel_inputs_channels[channel] = np.load(npy_full_path).squeeze()
        print(f'\tShape: {sel_inputs_channels[channel].shape}')
    
    # Stack the input arrays
    inputs = np.stack(list(sel_inputs_channels.values()), axis=3)
    print(f"Finish Process Inputs Channels: {inputs.shape}")
    
    # Select Taget Channels
    sel_target_channels = {}
    for channel, npy_path in target_channels.items():
        npy_full_path = npy_path if data_path is None else f'{data_path}/{npy_path}'
        print(f'\tLoading Target Channel ... {channel}:  {npy_full_path}')
        sel_target_channels[channel] = np.load(npy_full_path).squeeze()
        print(f'\tShape: {sel_target_channels[channel].shape}')

    # Stack the target arrays
    target = np.stack(list(sel_target_channels.values()), axis=3)
    print(f"Finish Process Target Channels: {target.shape}")
    
    if static_channels is not None:
        # Select Static Channels
        sel_static_channels = {}
        for channel, npy_path in static_channels.items():
            npy_full_path = npy_path if data_path is None else f'{data_path}/{npy_path}'
            print(f'\tLoading Static Channel ... {channel}: {npy_full_path}')
            sel_static_channels[channel] = np.load(npy_full_path).squeeze()
            print(f'\tShape: {sel_static_channels[channel].shape}')
        
        # Stack the input arrays
        static = np.stack(list(sel_static_channels.values()), axis=3)
        print(f"Finish Process Static Channels: {static.shape}")
        
        print(f'Inputs shape: {inputs.shape} & Static shape: {static.shape} & Target shape: {target.shape}')
        
        if as_dict:
            return{
                'inputs': inputs,
                'static': static,
                'target': target,
                }
        else:
            return inputs, static, target
    
    else:
        if as_dict:
            return{
                'inputs': inputs,
                'target': target,
                }
        else:
            return inputs, target

def sel_percentile_above(data_dict, mean_series_path=None, p=25, bound=None, for_val=False):
    """ 
    Select based on percentile indices
    """
    if mean_series_path is not None:
        fsum = np.load(mean_series_path)
        if for_val:
            fsum = fsum[bound:]
        else:
            fsum = fsum[:bound]
    else:
        if bound is None:
            target = data_dict['target']
        elif for_val:
            target = data_dict['target'][bound:]
        else:
            target = data_dict['target'][:bound]
        fsum = np.nanmean(target, axis=(1, 2))

    p_thresh = np.nanpercentile(fsum, p)
    p_idx = np.where(fsum >= p_thresh)[0]

    inputs = data_dict['inputs'][p_idx]
    static = data_dict['static'][p_idx]
    target = data_dict['target'][p_idx]

    return {
        'inputs': inputs, 
        'static': static, 
        'target': target
        }

def load_data_above_percentile(
        inputs_channels: dict,
        static_channels: dict,
        target_channels: dict,
        mean_series_path: str,
        p=None, 
        bound=12419, 
        for_val=False
        ):
    """
    Data Loader for above percentile threshold
    """
    
    data_dict = fetch_inputs_target_pairs(inputs_channels, static_channels, target_channels)
    
    if p is not None:
    
        data_dict = sel_percentile_above(data_dict, mean_series_path, p, bound, for_val)
               
    return data_dict['inputs'], data_dict['static'], data_dict['target']
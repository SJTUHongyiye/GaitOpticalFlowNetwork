conf = {
    "WORK_PATH": "./work",
    "CUDA_VISIBLE_DEVICES": "0,1,2,3",
    "data": {
        'dataset_path': "/lustre/home/acct-eejxh/eejxh/yhy/gait/DatasetB/videos",
        'resolution': '64',
        'dataset': 'CASIA-B',
        'pid_num': 73,
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,
        'lr': 1e-4,
        'hard_or_full_trip': 'full',
        'batch_size': (8, 16),
        'restore_iter': 0,
        'total_iter': 80000,
        'margin': 0.2,
        'num_workers': 3,
        'frame_num': 30,
        'model_name': 'GaitOpticalFlowNetwork',
    },
}

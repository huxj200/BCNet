from detectron2.data.datasets import register_coco_instances


def register_data():
    data_type = 'coco'
    if data_type == 'coco':
        register_coco_instances(name='self_coco_train', metadata={},
                                    json_file=r'/raid/users/hxj/datasets/logs/ann_train.json', 
                                    image_root='/raid/users/hxj/datasets/logs')

        register_coco_instances(name='self_coco_test', metadata={},
                                    json_file=r'/raid/users/hxj/datasets/logs/ann_test.json', 
                                    image_root='/raid/users/hxj/datasets/logs')
        
        register_coco_instances(name='self_cocosyn_train', metadata={},
                                    json_file=r'/raid/users/hxj/datasets/Real/train.json', 
                                    image_root='/raid/users/hxj/datasets/Real/train')
    # if data_type == 'coco':
    #     register_coco_instances(name='self_coco_train', metadata={},
    #                                 json_file=r'/raid/users/hxj/datasets/logs/train.json', 
    #                                 image_root='/raid/users/hxj/datasets/logs')

    #     register_coco_instances(name='self_coco_test', metadata={},
    #                                 json_file=r'/raid/users/hxj/datasets/logs/test.json', 
    #                                 image_root='/raid/users/hxj/datasets/logs')
        
    #     register_coco_instances(name='self_cocosyn_train', metadata={},
    #                                 json_file=r'/raid/users/hxj/datasets/Real/train.json', 
    #                                 image_root='/raid/users/hxj/datasets/Real/train')


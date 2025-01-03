## Simple decrator of tos download,process and upload
### Usage:
```
    from PIL import Image
    @tos_process_decorator()
    def process_data(local_file_path, *args, **kwargs):
        # 这里进行数据处理
        # 假设处理后的数据保存在临时文件中
        test_png = Image.open(local_file_path)
        return test_png

    # 调用装饰过的函数
    object_key = 'rendering/cam15/02a5ac47db6e09d5235bea600068dd0cdad7682dfa265d7052c247e3d21abf88/View5_SceneDepth.png'
    tos_prefix = 'rendering/cam15/02a5ac47db6e09d5235bea600068dd0cdad7682dfa265d7052c247e3d21abf88/'
    output_key = 'View5_SceneDepth_test.png'
    suffix = '.png'
    process_data(object_key=object_key,suffix=suffix, tos_prefix=tos_prefix, output_key=output_key)
```
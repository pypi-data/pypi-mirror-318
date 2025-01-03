# 定义类型和对应的符号
type_mapping = {
    'uint8_t': 'u1',
    'uint16_t': 'u2',
    'uint32_t': 'u4',
    'uint64_t': 'u8',
    'int8_t': 'i1',
    'int16_t': 'i2',
    'int32_t': 'i4',
    'int64_t': 'i8',
    'float': 'f4',
    'double': 'f8',
    'std::array<char, 8>': 'S8',
    'std::array<char, 16>': 'S16',
    'std::array<char, 32>': 'S32',
    'std::array<char, 64>': 'S64',
    'std::array<char, 128>': 'S128',
    'std::array<char, 256>': 'S256',
}

py_name = '_phm'
# 定义特殊的类型组合
dict_types = list(type_mapping.keys())
set_types = list(type_mapping.keys())
multidict_types = list(type_mapping.keys())

# 生成 C++ 和 Python 代码模板
cpp_code = "#include \"phashmap.cpp\"\n#include <pybind11/pybind11.h>\nPYBIND11_MODULE(_phashmap, m) {\n"
python_code = "import numpy as np\nimport _phashmap as _phm\ndict_types = {\n"

# 在一个for循环中生成C++和Python代码
for t1 in dict_types:
    for t2 in dict_types:
        # C++ declare_dict
        type1,type2 = type_mapping[t1],type_mapping[t2]
        dict_name = f"Dict_{type1}_{type2}"
        cpp_code += f"\tdeclare_dict<{t1}, {t2}>(m, \"{dict_name}\");\n"
        # Python dict_types
        python_code += f"    (np.dtype('{type1}'), np.dtype('{type2}')) : _phm.{dict_name},\n"

cpp_code += "\n"
python_code += "}\n\n"

# 生成 declare_set 和 Python set_types
python_code += "\nset_types = {\n"
for t in set_types:
    # C++ declare_set
    type1 = type_mapping[t]
    set_name = f"Set_{type1}"
    cpp_code += f"\tdeclare_set<{t}>(m, \"{set_name}\");\n"
    # Python set_types
    python_code += f"    np.dtype('{type1}') : _phm.{set_name},\n"
cpp_code += "\n"
python_code += "}\n\n"

# 生成 declare_multidict 和 Python multidict_types
python_code += "multidict_types = {\n"
for t1 in multidict_types:
    for t2 in multidict_types:
        # C++ declare_multidict
        type1, type2 = type_mapping[t1], type_mapping[t2]
        multidict_name = f"MultiDict_{type1}_{type2}"
        cpp_code += f"\tdeclare_multidict<{t1}, {t2}>(m, \"{multidict_name}\");\n"
        # Python multidict_types
        python_code += f"    (np.dtype('{type1}'), np.dtype('{type2}')) : _phm.{multidict_name},\n"
cpp_code += "}"
python_code += "}\n"

# 输出到 C++ 文件
with open("phashmap_types_generated.cpp", "w") as cpp_file:
    cpp_file.write(cpp_code)

print("C++ header file has been generated!")

# 输出到 Python 文件
with open("phashmap_types_generated.py", "w") as py_file:
    py_file.write(python_code)

print("Python code for types has been generated!")

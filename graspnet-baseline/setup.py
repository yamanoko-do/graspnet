from setuptools import setup, find_namespace_packages

# 读取requirements.txt中的依赖
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# 查找并打印包
packages=find_namespace_packages()
print("找到的包:")
for package in packages:
    print(f"- {package}")

setup(
    name="graspnetbaseline",
    version="0.1.0",
    packages=packages, 
    install_requires=requirements,
)
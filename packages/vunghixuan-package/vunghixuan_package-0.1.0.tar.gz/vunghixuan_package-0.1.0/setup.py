# setup.py

from setuptools import setup, find_packages

setup(
    name='vunghixuan_package',
    version='0.1.0',
    description='API, OTP, Create Project',
    author='Đăng Thanh Vũ',
    author_email='vunghixuan@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['python-dotenv','requests'],  # Các gói phụ thuộc
    entry_points={
        'console_scripts': [
            'vunghixuan_package=vunghixuan_package.main:main'
        ]
    }
)


"""
Quy trình phát hành gói Python bao gồm nhiều bước quan trọng, mỗi bước đều có chức năng riêng biệt:

1. pip install .: Lệnh này được sử dụng để cài đặt gói Python từ thư mục hiện tại. Nó sẽ tìm kiếm file setup.py và cài đặt gói theo cấu hình đã định nghĩa.

2. python setup.py sdist bdist_wheel: Lệnh này tạo ra các gói phân phối. sdist tạo ra gói nguồn, trong khi bdist_wheel tạo ra gói nhị phân (wheel). Điều này giúp người dùng có thể cài đặt gói một cách dễ dàng hơn.

Vào folder dist lấy thông tin file và: Sau khi tạo gói, bạn cần vào thư mục dist để tìm file gói đã tạo.

3. pip install dist/vunghixuan-0.1-py3-none-any.whl: Lệnh này cài đặt gói đã được tạo ra từ thư mục dist.

4. Cập nhật nếu hỏi: pip install dist/vunghixuan-0.1-py3-none-any.whl --force-reinstall: Nếu bạn cần cập nhật gói đã cài đặt, lệnh này sẽ cài đặt lại gói, bất kể phiên bản hiện tại.

5. twine upload dist/*: Cuối cùng, lệnh này được sử dụng để tải lên gói đã tạo lên PyPI, giúp người khác có thể cài đặt gói của bạn dễ dàng.
Tóm lại, bước 1 và 2 tạo môi trường local, trong khi bước 5 là bước tải lên gói lên PyPI.

"""

# pypi-AgEIcHlwaS5vcmcCJGRmOTZjMWEwLTg3YjEtNDQ4My1iMzc3LTVmZmIxMzdiYzkxMgACKlszLCI4OWIwMTU4NS0wNzFhLTQ1M2ItYTU2Yi1lMjU2YTAyYzUzMzkiXQAABiCqSM0HmXMCrq31YYQOx_5Up0gQaH0xbg21VpYen9CKlw
"""
[pypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmcCJGRmOTZjMWEwLTg3YjEtNDQ4My1iMzc3LTVmZmIxMzdiYzkxMgACKlszLCI4OWIwMTU4NS0wNzFhLTQ1M2ItYTU2Yi1lMjU2YTAyYzUzMzkiXQAABiCqSM0HmXMCrq31YYQOx_5Up0gQaH0xbg21VpYen9CKlw
"""

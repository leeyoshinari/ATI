# ATI
The implementation of Automated Testing of Interfaces.

## Usage
1. Clone ATI repository
   ```shell
   git clone https://github.com/leeyoshinari/ATI.git
   cd ATI
   ```

2. Modify `./common/GenerateKey.py`. It's used to encrypt your password of email.

3. Modify `config.py`.
   
4. Design test cases. Modify `globalVariables.txt` and `testCase.xlsx`.<br>
   (1) In `globalVariables.txt`, it stores global variables, the format is `variable_name variable_value`, splited by `space`.<br>
   (2) In `testCase.xlsx`, parameters need to be parameterized, variables must be identified with `<>`, for example: `<variable_name>`.<br>
   
5. Run
   ```shell
   python3 main.py
   ```
   or
   ```shell
   nohup python3 main.py &
   ```

6. For more information, please [readme](https://blog.csdn.net/leeyoshinari/article/details/97612522).

## Requirements
1. requests
2. xlrd
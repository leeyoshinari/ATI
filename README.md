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
   (2) In `testCase.xlsx`, parameters need to be parameterized, variables must be identified with `#`, for example: `#variable_name#`.<br>
   (3) In `testCase.xlsx`, the column of `I` and `J`, if only judge whether response value contains a text, please set column of `J`, if judge whether full response value is right, please set column of `I`, default use column of `J`.

5. Run
   ```shell
   python3 main.py
   ```
   or
   ```shell
   nohup python3 main.py &
   ```

## Requirements
1. requests
2. xlrd
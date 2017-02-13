# Install Octave

- Mac

System Perferences > search "Gatekeeper" > General > Allow apps download from Anywhere

Download Octave installer > Install Octave

binaries: /usr/local/octave/3.8.0

Applications(x2):
/Applications/Octave-cli.app
/Applications/Octave-gui.app

# Multivariate Linear Regression

Multiple Features: h_theta(x) = theta0 * x0 + theta1 * x1 + theta2 * x2 ....,   x0 =1	=> transpose of matrix (theta) * matrix(x), Multivariate linear regression

# Gradient Descent for Multiple Variables

note: x_a^i = x + superscript i + subscript a

Cost Function: J(theta) = Least Square, 最小平方差法 = 1 / 2m * SUM ( h_theta(x^i) ^ 2 - y^i ^ 2 ), i = 1~m

Gradient Descent, 梯度下降法: theta_j := theta_j - alpha / 2m * d(J(theta)) / d(theta_j) => theta_j := theta_j - alpha / m * SUM ((h_theta(x^i) - y^i) * x_j^i)

# Gradient Descent in Practive

Feature Scaling: 

Get feature -1 < x_i < 1 approximately, will let gradient descent be easy

Mean normalization: let x_i => x_i - mu_i close to zero

=> x_i => (x_i - mu_i) / s_i, mu_i = average; s_i = standard deviation

Learning Rate (alpha):

J(theta) should decrease after every iterations

Plot J(theta) vs. No. of iterations : make sure alpha sufficiently small but not let gradient descent be slow to converge

# Features and Polynomial Regression

Change the behavior of the hypothesis to fit the data well 

model: quadratic, cubic, square root... (automatically choice?)

# Normal Equation

theta = Inverse(X_transpose * X) * X_transpose * y

Octave: pinv(X' * X) * X' * y, pinv: pseudo-inverse

m: training examples; n: features

n < 10000 : Normal eq'n; n > 10 ^ 6: gradient descent

# Octave Tutotial

## Basic Operations

1 == 2 % false, equal(==); comment(%)

1 ~= 2 , not equal(~=)

1 && 0 % false, and(&&)

1 || 0, or(||)

PS1('>> '): change the prompt

a = 3; % semicolon supressing output

a = pi;

disp(a) >> 3.1416; 

disp(sprintf('2 decimals: %0.2f'  a)) >> 3.14

disp(sprintf('6 decimals: %0.6f'  a)) >> 3.141593

A = [1 2; 3 4; 5 6], 3 by 2 vector

v = [1 2 3], 1 by 3 vector; v = [1, 2, 3], 3 by 1 vector

v = 1:6, v = 1 2 3 4 5 6

v = 1:0.1:1.4, v = 1.0 1.1 1.2 1.3 1.4

v = ones(2,3), 2 by 3 matrix of 1

w = rand(1,4), 1 by 4 random martix

w = randn(1,10000), 10000 term of normal disturbution(gaussian distribution)

hist(w), 將w以長條圖表示

hist(w,50), 50條bins, 長條

eye(4), 4 by 4 單位矩陣

## 常用cmd, move data around

size(A) >>  3 2

size(A,1) >> 3

size(A, 2) >> 2

v = [1 2 3 4]

length(v) >> 4

length(A) >> 3, longer dimension

ls, pwd, cd same as UNIX

load('dat_file'): 變數載入.dat檔

who: 展示所存變數

whos: details

clear, 清空儲存變數

save xxx.mat v: 將v變數存成xxx.mat於資料夾

save xxx.txt v -ascii: 將v變數存成xxx.mat並用ascii,可讀

A(1,3): index first row, third column; A(:,2): all in second column; A([1 3],:): all in first and third row; A(:): put all elements of A into a single vector

A(:,2) = [10; 11; 12], assign second column; A = [A , [100; 101; 102]], append

A,B = 3*2 matrix => C = [A B] = [A,B], 3*4 matrix; C = [A; B], 6*2 matrix, semicolon= to the bottom

# Computing on Data

A_32 * B_22: matrix multiply; A_32 .* B_32: multiply by the corresponding element

A .^ 2, 1 ./ A: "."operate on each elements

log(v), exp(v), abs(v): elements-wise operation too

v + 1: elements-wise, each term add 1

A': transpose

magic(3), magic square 3*3

sum(a): sum all elements; prod(a): multiply all; max(rand(3), rand(3)): choose large one

max(A,[],1): find maxium per column; max(A,[],2): find maxium per row; max(max(A)) = max(A(:)): find max element

filpud(): filp up down

pinv(): pseudo inverse

# Plot result

plot(x,y); 

hold on; plot(t, y1); plot(t, y2, 'r'): show 2 figures on same plot

xlabel('time'); ylabel('value'); legend('sin', 'cos'); title('my plot')

print -dpng 'myplot.png': save figure

subplot(1,2,1); plot(t, y1)

axis([0.5 1 -1 1]): set x-axis=0.5~1, y-axis=-1~1

clf = clear figure

imagesc(A); colorbar; colormap gray: make color image, add value-color bar, 灰階

# Control, 判斷

## for loop

for i=1:10, (or indice=1:10; for i=indice,)

    v(i) = 2^i;

end;

v = 2的1~10次方, 注意"," 和 ";"

## while loop

i=1;

while true,

    v(i) = 999;

    i = i+1;

    if i == 6,

        break;

    end;

end;

v = 999(x5), 64, 128 .....1024, 修改前五項

## if, elseif, else

v(1) = 2;

if v(1) = 1,

    disp('one');

elseif v(1) = 2,

    disp('two');

else

    disp('no one/two');

end;

two, else後不需加','

## lib檔

in Octave program

addpath('/path/to/file/directory')

即可呼叫file內的method

### example

costFunctionJ.m:

fuction J = costFunctionJ(X, y, theta)

% X = "design matrix", training examples

% y = class label

m = size(X, 1); % num. of training examples

predictions = X*theta; % linear prediction

sqrErrors = (predictions-y) .^2;

J = 1/(2*m) * sum(sqrErrors);

run:

X = [1 1; 1 2; 1 3]

y = [1; 2; 3]

theta = [0;1];

j = costFuctionJ(X, y, theta)

回傳 j = 0, 符合linear假設

# Vectorization

## Unvectorized implementation

prediction = 0.0;

for j = 1:n+1,
    
    prediction = prediction + theta(j) * x(j)

end;

## Vectorized implemetation

prediction = theta' * x;

## Gradient descent

for j = 1:n+1,

    for i = 1 + m,

        theta(j) = theta(j) - alpha * delta(i) * x(i);
    
    end;

end;

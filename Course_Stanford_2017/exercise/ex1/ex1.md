# ex1

## 1

回傳5x5單位矩陣

A = eye(5);

## 2

### 2.1 作圖：

    data = load('ex1data1.txt');

    X = data(:, 1); y = data(:, 2); % 自ex1data1.txt載入數據,給X,y值

    m = length(y); %  訓練組數

    plotData(X, y); % 將X,y帶入plotData方法

修改plotData.m

    plot(x, y, 'rx', 'MarkerSize', 10) % 畫大小10的紅叉

    ylabel('Profit in $10,000s')

    xlabel('Population of City in 10,000s')

### 2.2 Gradient descent

    X = [ones(m, 1), data(:,1)]; % X加上常數項

    theta = zeros(2, 1); % initialize fitting parameters

    iterations = 1500;

    alpha = 0.01; % 設定參數

    computeCost(X, y, theta)  % computeCost

    theta = gradientDescent(X, y, theta, alpha, iterations);

computeCost.m

    predictions = X * theta;

    sqrErrors = (predictions - y) .^ 2;

    J = 1 / (2 * m) * sum(sqrErrors); % costfuction

gradientDescent.m

    prediction = X * theta;

    theta(1) = theta(1) - alpha/m .* sum((prediction - y) .* X(:,1))

    theta(2) = theta(2) - alpha/m .* sum((prediction - y) .* X(:,2)) % 常數項與一次項的係數依迭代修正 


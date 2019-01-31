---
layout: post
title: "Epoch과 Batch와 Iteration에 관하여"
date: 2019-01-23
---

머신러닝을 공부하다보면 Epoch, Batch, Iteration 같은 개념들을 만나게됩니다. 각각의 개념이 가지는 의미와 어디에서 쓰이는 지 알아보기 위하여
[여기](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)에 있는 정보를 가지고 공부한 내용을 정리하여 보았습니다.

### Gradient Descent
Gradient Descent는 머신러닝에서 최적의 결과를 찾기위한 iterative한 방법의 최적화 알고리즙입니다.
알고리즘이 iterative 하다는 것은 최적의 결과를 값을 얻기 위하여 여러 번의의 연산을 진행하여 결과를 얻는 다는 것을 의미합니다.
Gradient Descent는 말 그대로 경사를 따라서 내려가는 알고리즘입니다. 우리가 머신러닝을 공부하다보면 Cost 함수나
Loss 함수를 정의하여 사용하는 것을 볼 수 있습니다 Cost(Loss) 함수는 알고리즘의 목적이 되는 함수로써 이것을
최소화하는 것으로 문제를 해결해 나갑니다. 일반적인 Cost 함수는 왼쪽 그림과 같이 나타나는데 이때 Gradient Descent
알고리즘을 이용하여 그래프의 경사면을 하강해 내려가면서 최적화의 값을 찾는 방향으로 학습을 진행합니다. gradient descent와 같은
최적화 알고리즘에는 learning rate라는 값을 필요로 합니다. learning rate란 쉽게 말해서 경사면을 내려가는 정도를 조정하는
값입니다. 이 값이 커질수록 알고리즘 상에서 경사를 빠르게 내려가지만 최적화 값에 수렴하지 못하고 값이 발산해버리는
overshooting과 같은 문제가 발생할 수 있습니다. 반대로 이 값을 작게 설정할 수록 알고리즘 상에서 경사를 느리게 내려가기 
때문에 최적화 값을 얻기 위해 필요한 학습의 횟수가 늘어나게 됩니다.
![img](https://cdn-images-1.medium.com/max/800/1*KQVi812_aERFRolz_5G3rA.gif)

### Epochs
*한 번의 Epoch은 전체 데이터 셋을 알고리즘에 한 번 전달하는 것을 의미합니다*

일반적으로 머신러닝 알고리즘을 진행할 때에는 한 번의 학습으로는 최적의 결과값을 얻는 것이 어렵기 때문에
여러번의 Epoch으로 알고리즘을 실행시킵니다. Epoch이 진행될수록 모델은 점점 최적화가 진행되어 충분한 
Epoch이 진행된 후에는 최적의 모델을 찾을 수 있게 됩니다. 적절한 Epoch의 수는 데이터와 모델에 따라
달라지기 때문에 학습을 통하여 얼마만큼의 Epoch이 필요한지 알아내야 합니다. 흔히 사용되는 방법으로는 
정확도가 더 이상 올라가지 않거나 유의미한 변화를 보이지 않는 경우 종료하는 방법이 있습니다.

### Batch size
컴퓨터가 한 번에 처리할 수 있는 데이터의 양은 한정되어 있기 때문에 우리는 하나의 Epoch을 진행할 때 여러개의
Batch로 나누어서 학습을 진행하게 됩니다. 이 때 하나의 Batch에서 제공하는 데이터 셋의 개수를 batch size
라고 합니다. 이 batch size를 조절함에 따라서 학습 속도, 학습 결과등이 달라지기 때문에 적절한 batch size를
정하는 것이 중요합니다. 적절한 batch size를 정하는 법에 대해서 다양한 연구들이 진행되었습니다

### Iteration
Iteration은 말그대로 학습을 반복하는 횟수를 의미합니다. Iteration은 batch size 와 관련이 있는데
예를 들어 n개의 데이터에 대해서 학습을 진행할때 배치 사이즈를 m으로 잡는다면 Iteration의 횟수는 n/m이 됩니다
즉 batch size가 커질 수록 iteration의 크기는 작아지게 됩니다

머신러닝을 진행할 때에는 위에 설명한 요소들을 이용하여 모델을 학습을 시킵니다. 더 좋은 결과를 내기 위하여
적절한 Epoch, batch size(iteration), learning rate를 찾아 내는 과정이 필요합니다


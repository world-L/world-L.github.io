---
layout: post
title: "Epoch과 Batch와 Iteration에 관하여"
date: 2019-01-23
---

머신러닝을 공부하다보면 Epoch, Batch, Iteration 같은 개념들을 만나게됩니다. 각각의 개념이 가지는 의미와 어디에서 쓰이는 지 알아보기 위하여
[여기](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)에 있는 정보를 가지고 공부한 내용을 정리하여 보았습니다.

### Gradient Descent
Gradient Descent는 머신러닝에서 최적의 결과를 찾기위한 iterative한 방법의 최적화 알고리즙입니다.
알고리즘이 iterative 하다는 것은 최적의 결과를 값을 얻기 위하여 여러 번의 결과를 얻는 다는 것을 의미합니다.

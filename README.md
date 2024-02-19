# 자료구조와 알고리즘
부경대 IoT 개발자 파이썬 자료구조와 알고리즘 학습 리포지토리

## 1일차
- 자료구조, 알고리즘 개요
- 파이썬 기초 복습, 함수까지

## 2일차
- 파이썬 기초 복습
    - 가변형 mutable -> 배열(리스트), 딕셔너리, 세트 / 불변형 immutable -> 문자열, 튜플


    ![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C)


- 파이썬 자료구조
    - 선형 리스트(배열)
    - 단순 연결 리스트 = 파이썬의 list와 동일 

    ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png)


## 3일차
- 파이썬 자료구조
    - 단순 연결 리스트 다시
    - 원형 연결 리스트 : 마지막 노드가 첫 노드와 연결
    - 스택 : 한쪽 끝이 막힌 형태 -> 입구가 하나이기 때문에 먼저 들어간 것이 가장 나중에 나오는 구조(선입후출, 후입선출) / Last In First Out(LIFO)
        - pop - list.pop()
        - push - list.append() 와 동일
        
    ![stack](https://cs.lmu.edu/~ray/images/stack.gif)

    - 큐 : First In First Out(FIFO) -> 입구와 출구가 따로 있는 원통 형태
    ![queue](https://raw.githubusercontent.com/qkrskdusdlqslek/ds-and-algorithm/main/images/queue.png)
        

## 4일차
- 파이썬 자료구조
    - 큐 다시
    - 이진 트리

    ![이진트리](https://kahee.github.io//assets/post_img/tree3.png)

## 5일차
- 파이썬 자료구조 / 알고리즘
    - 그래프 : Depth First Search(DFS)/ Breadth First Search(BFS)
    

    ![그래프 개념](https://raw.githubusercontent.com/qkrskdusdlqslek/ds-and-algorithm/main/images/graph02.png)

## 6일차
- 파이썬 자료구조/ 알고리즘
    - 재귀호출 (무한반복처럼 보이지만 무한반복이 아님)
    - 정렬
        - 선택정렬 Selection Sort - 최소값을 찾아서 맨 앞으로 보내는 정렬 O(n^2)
        - 삽입정렬 Insertion Sort - 기준값 기준으로 앞,뒤로 보내는 정렬 O(n^2)
        - 버블정렬 Bubble Sort - 기준값 기준으로 제일 큰값을 뒤로 보내는 정렬 O(n^2)
        - 퀵정렬   Quick Sort - 기준값 기준으로 작은값 그룹이랑 큰값 그룹을 분리한 뒤 다시 정렬 재귀호출 O(nlongn) -> 제일 빠름

## 7일차
- 코딩테스트
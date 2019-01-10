#ifndef LIST_H
#define LIST_H

#include <iostream>
using namespace std;

#include "Event.h"
#include "Array.h"

template <class T>
class List
{
    class Node{
        friend class List<T>;
        private:
            T event;
            Node* next = NULL;
    };
    public:
        List();
        ~List();
        void add(T);
        void print();
        void format(string& outStr);
        void copy(Array& arr);
    private:
        Node* head;
    
};


template <class T>
List<T>::List()
{
  head = NULL;
}

template <class T>
List<T>::~List()
{
  Node *currNode, *nextNode;

  currNode = head;

  while (currNode != NULL) {
    nextNode = currNode->next;
    delete currNode->event;
    delete currNode;
    currNode = nextNode;
  }
}


template <class T>
void List<T>::add(T newEvent){
    Node* newNode = new Node();
    newNode->event = newEvent;
    newNode->next = head;
    head = newNode;
    Node* currentNode = head;
    T temp = NULL;

    while(currentNode->next!=NULL){
        if (*(currentNode->next->event)<(currentNode->event)){
            temp = currentNode->next->event;
            currentNode->next->event = currentNode->event;
            currentNode->event = temp;
        }
        currentNode = currentNode->next;
    }
}

template <class T>
void List<T>::print(){
    Node *currNode;
    currNode = head;
    while (currNode != NULL) {
        currNode->event->print();
        currNode = currNode->next;
  }

}

template <class T>
void List<T>::format(string& outStr){
    Node *currNode;
    currNode = head;
    while (currNode != NULL) {
        currNode->event->format(outStr);
        currNode = currNode->next;
  }
}

template <class T>
void List<T>::copy(Array& arr){
    Node *currNode;
    currNode = head;
    while (currNode != NULL) {
        arr.add(currNode->event);
        currNode = currNode->next;
  }
}

#endif

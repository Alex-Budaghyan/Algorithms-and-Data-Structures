#include <iostream>
#include "BinaryTree.h"

int main()
{
    BinaryTree<int> tree;

    tree.insertR(20);
    tree.insertI(10);
    tree.insertR(30);
    tree.insertR(9);
    tree.insertI(15);
    tree.insertR(16);
    tree.insertR(7);
    tree.insertR(14);
    tree.insertI(25);
    tree.insertI(7);
    tree.insertR(15);
    tree.insertR(6);
    tree.insertR(13);

    // tree.setNodeToLeafCountI();
    std::cout << "\npreorder iterative:  ";
    tree.preorderI();
    std::cout << "\nMax data at level Iterative: ";
    tree.maxOfLevelI();
    std::cout << "\nMax data at level Recursive: ";
    tree.maxOfLevelR();

    std::cout << "\nMin data at level Iterative: ";
    tree.minOfLevelI();
    std::cout << "\nMin data at level Recursive: ";
    tree.minOfLevelR();

    std::cout << "\nLevels with the maximum count Iterative: ";
    tree.maxCountLevelI();
    std::cout << "\nLevels with the maximum count Recursive: ";
    tree.maxCountLevelR();

    std::cout << "\nCount of Leaves Recursive: " << tree.countOfLeavesR();
    std::cout << "\nCount of Leaves Iterative: " << tree.countOfLeavesI() << std::endl;

    std::cout << "\nCount of Nodes with two childrens Iterative: " << tree.countNodesWithTwoChildrenI();
    std::cout << "\nCount of Nodes with two childrens Recursive: " << tree.countNodesWithTwoChildrenR() << std ::endl;

    std::cout << "\nCount of Nodes with one childrens Iterative: " << tree.countNodesWithOneChildI();
    std::cout << "\nCount of Nodes with one childrens Recursive: " << tree.countNodesWithOneChildR() << std ::endl;

    std::cout << "\nHeight of Tree Recursive: " << tree.heightR();
    std::cout << "\nHeight of Tree Iterative preorder: " << tree.height_preorderI();
    std::cout << "\nHeight of Tree Iterative levelorder: " << tree.height_levelorderI();

    std::cout << "\nLeaves in inorder traversal Iterative: ";
    tree.printLeavesInorderI();
    std::cout << "\nLeaves in inorder traversal Recurisve: ";
    tree.printLeavesInorderR();
    
    // tree.setNodeToLeafCountI();
    // std::cout <<"\nAfter set Nodes Iterative: ";
    // tree.preorderI();
    // tree.setNodeToLeafCountR();
    // std::cout << "\nAfter set nodes Recurisve: ";
    // tree.preorderI();

    std::cout << "\ntree constainsR 55: " << std::boolalpha << tree.containsR(55) << std::endl;
    std::cout << "tree constainsI 55: " << std::boolalpha << tree.containsI(55) << std::endl;
    std::cout << "tree constainsR 15: " << std::boolalpha << tree.containsR(15) << std::endl;
    std::cout << "tree constainsI 15: " << std::boolalpha << tree.containsI(15) << std::endl;
    std::cout << "tree constainsR -5: " << std::boolalpha << tree.containsR(-5) << std::endl;
    std::cout << "tree constainsI -5: " << std::boolalpha << tree.containsI(-5) << std::endl;

    std::cout <<"\npreorder recoursive: ";
    tree.preorderR();

    std::cout << "\npreorder iterative:  ";
    tree.preorderI();

    std::cout << "\ninorder recoursive: ";
    tree.inorderR();

    std::cout << "\ninorder iterative:  ";
    tree.inorderI();

    std::cout << "\npostorder recoursive: ";
    tree.postorderR();

    std::cout << "\npostorder iterative:  ";
    tree.postorderI();

    std::cout << "\nlevelorder iterative:  ";
    tree.levelorder();

    std::cout << "\nCount of Nodes: " << tree.countOfNodesR();
    std::cout << "\nCount of Leaves: " << tree.countOfLeavesR();

    std::cout << "\nHeight of Tree: " << tree.heightR();
    std::cout << "\nWidth of Tree: " << tree.widthI();
    std::cout << "\nMax of Tree: " << tree.findMaxI();
    std::cout << "\nMin of Tree: " << tree.findMinR();

    std::cout << "deleting 7 15 20" << std::endl;

    tree.eraseR(7);
    tree.eraseR(15);
    tree.eraseR(20);
    tree.eraseR(15);


    std::cout << "\ninorder recoursive after deleting nodes: ";
    tree.inorderR();

    std::cout << "\nlevelorder iterative:  ";
    tree.levelorder();

    tree.clearR();

    std::cout << "\npostorder after clearing: ";
    tree.postorderR();

    return 0;
}

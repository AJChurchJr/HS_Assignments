/*THIS PROJECT IS NOT 100% FINISHED!! I HAVE CREATED A METHOD THAT MAKES THE SOLVING METHOD COMPLETELY RANDOM. THIS MEANS THAT THE FUNCTION ITSELF IS NOT OPTIMIZED AND IS NOT THE BEST WAY TO SOLVE THE PUZZLE. I SPENT A MAJORITY OF MY TIME WORKING ON THE ENGINE AROUND IT.*/


/* PLEASE NOTE THAT THE PSEUDOCODE HAS CHANGED A LOT IN THE ACTUAL CODE. I DID NOT STEAL ANYONE ELSE'S STUFF, IT'S JUST THAT THE PSEUDOCODE WAS NOT SUFFICIENT FOR SOME THINGS THAT CAME UP.
 (DONE) Create universal variables
 -(int) ring_amount
 -(int) tower_target (1,2,3)
 -(int) begin_tower (1,2,3)
 
 -Create universal functions
 -(void) transfer_ring
 (takes in argument of the tower giving and the tower receiving)
 (the ring being used it automatic -- it is simply the highest ring of the tower giving)
 (once it saves the highest ring, it will delete it from the tower giving)
 (this might also use highest_ring_index)
 (it then uses it as an argument within add_ring for the tower receiving)
 (done)
 
 (DONE) Create class for ring
 -Variables:
 -(int) size
 
 -Create class for tower
 -Variables:
 (DONE) (ring) ring_array
 (Array with each ring object inside of it)
 -(int) highest_ring_size
 (Auto-defined integer containing the size of the uppermost ring)
 (this is to make sure nothing larger goes on top)
 (defaults at 0, which means there are no rings on the tower)
 (DONE) (int) highest_ring_index
 (integer that allows for update_highest_ring_size to determine which index the highest ring is located)
 (defaults at 0, which means there are no rings on the tower)
 -Methods:
 -(void) add_ring
 (takes in a ring object as an argument
 (if the ring's size variable is smaller than highest_ring_size, it will allow it to be appended to the end of the list)
 (it will then run update_highest_ring_size)
 (if not, it simply passes)
 -(void) remove_ring
 (removes the highest ring) (only does this if highest_ring_index is greater than 0)
 (runs update_highest_ring_size)
 -(void) update_highest_ring_size
 (goes to the index of highest_ring_index of ring_array, and fetches the size variable of the ring
 
 -Create a repeating function needed to auto-solve the method
 -Due to input validation, which will deny a function if it does not work (like if a bigger ring gets stacked onto a smaller ring), so anything can be run and it can kind of just randomly guess the solution
 -To put it simple
 -Constantly run the "transfer ring" command
 -(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)
 -OVER AND OVER AND OVER
 
 (upon revision, this did not work as planned)
 
 */



#include <iostream>
//#include <Windows.h>
#include <stdlib.h>
using namespace std;


class tower
{
public:
    //contruction method
    int highest_ring_index = 0; // The index of the highest ring (how many rings are on the tower) (to use properly with indexing, subtract one from the value)
    int* ring_array; // The array containing every ring on the tower; the number contained is the size
    int max_ring_length = 0; // Error prevention in case if more than the highest amount of rings SOMEHOW appears
    
    tower(bool correct, int ringLen)
    {
        //cout << "--------------------" << endl;
        max_ring_length = ringLen;
        
        //This only modifies values if the results given are one or the other.
        //This is because, if you modify values with ringLen, and the tower is not the one targeted, every tower will have rings and will, in turn, break.
        if (correct)
        {
            //variable creation
            highest_ring_index = ringLen;
            //creating ring array
            ring_array = new int[ringLen]; //size of array does not need to be subtracted, only index
            
            //make a for-loop, starting from 0 counting up to the length of highest_ring_index MINUS ONE
            //for each one, add the value of i to ring_array
            for (int i = 0; i <= (highest_ring_index - 1); ++i)
            {
                ring_array[i] = i + 1;
                //cout << "CURRENT INDEX: " << i << "|" << "CURRENT RING SIZE: " << ring_array[i] << endl;
            }
            //cout << endl << "HIGHEST VALUE: " << highest_ring_index << "|" << "HIGHEST INDEX: " << highest_ring_index - 1 << endl;
            return;
        }
        //defining other variables if this is not the beginning tower
        else{
            highest_ring_index = 0;
            ring_array = new int[ringLen];
        }
        //QUICK NOTE
        //When a value is deleted off of the ring_array, the size will simply be replaced with 0.
        
        
    }
    
    bool remove_ring() //a return of True means that the task could be completed, and a return of False means the opposite.
    {
        if (highest_ring_index > 0) {
            cout << "Removing ring at index " << highest_ring_index - 1 << " with size " << ring_array[highest_ring_index - 1] << "...";
            ring_array[highest_ring_index - 1] = 0;highest_ring_index--;
            cout << "success!" << endl;
            return true;
        }
        else { cout << "CANNOT REMOVE: array is empty." << endl; return false; }
    }
    bool add_ring(int size = 0)//a return of True means that the task could be completed, and a return of False means the opposite.
    {
        //DOUBLE CHECKING FOR ERRORS -- WHICH IT ONLY DOES IF THE RING ARRAY IS NOT EMPTY
        if (highest_ring_index != 0)
        {
            if (size == 0) { cout << "CANNOT ADD: size not provided." << endl; return false; }
            else if ((size > ring_array[highest_ring_index - 1]) && (ring_array[highest_ring_index - 1] > 0))
            {
                cout << "CANNOT ADD: ring too large." << endl;
                return false;
            }
            else if (highest_ring_index > max_ring_length - 1) {
                cout << "CANNOT ADD: maximum ring limit reached." << endl;
                return false;
            }
            //ACTUAL CODE
            else if (size != 0 || size < ring_array[highest_ring_index - 1])
            {
                cout << "Adding ring to index of " << highest_ring_index << " with size " << size << "...";
                ring_array[highest_ring_index] = size;
                highest_ring_index++;
                cout << "success!" << endl;
                return true;
            }
        }
        //DUPLICATE OF ACTUAL CODE, WHICH WORKS DIFFERENTLY DUE TO THE FACT THAT THE RING ARRAY IS EMPTY.
        else if (highest_ring_index == 0)
        {
            cout << "Adding ring to index of " << highest_ring_index << " with size " << size << "...";
            ring_array[highest_ring_index] = size;
            highest_ring_index++;
            cout << "success!" << endl;
            return true;
        }
        
        return false; //panic code
    }
    void display_array() //does not return anything; only displays
    {
        for (int i = 0; i <= (highest_ring_index - 1); ++i)
        {
            cout << "@ " << "INDEX:" << i << "|SIZE:" << ring_array[i] << " @";
        }
        cout << endl;
    }
    
    
    
    
};

void display_rings(tower &tower1, tower &tower2, tower &tower3, int counter = 1)
{
    cout << "TOWER 1" << endl;
    cout << "|" << endl;
    cout << "-"; for (int i = 0; i <= (tower1.highest_ring_index - 1); ++i) { cout << tower1.ring_array[i] << "-"; } cout << endl;
    cout << "|" << endl;
    cout << "TOWER 2" << endl;
    cout << "|" << endl;
    cout << "-"; for (int i = 0; i <= (tower2.highest_ring_index - 1); ++i) { cout << tower2.ring_array[i] << "-"; } cout << endl;
    cout << "|" << endl;
    cout << "TOWER 3" << endl;
    cout << "|" << endl;
    cout << "-"; for (int i = 0; i <= (tower3.highest_ring_index - 1); ++i) { cout << tower3.ring_array[i] << "-"; } cout << endl;
    cout << "|" << endl;
    
}
void swap_rings(tower &giver, tower &reciever)
{
    cout << "-------------------" << endl << "BEGINNING TRANSFER..." << endl;
    int midTransfer = giver.ring_array[giver.highest_ring_index - 1];
    cout << "RING TRANSFER SIZE: " << midTransfer << endl;
    bool correct = giver.remove_ring(); //takes ring from giver
    if (not correct) { cout << "TRANSFER CANCELLED!" << endl; return; }
    correct = reciever.add_ring(midTransfer); //attempt to give ring to receiver
    if (not correct) {cout << "TRANSFER CANCELLED!" << endl; giver.add_ring(midTransfer);} //returns ring to giver
    cout << "TRANSFER COMPLETE!" << endl;
    return;
}
bool check_if_complete(int targetNum, tower tower1,tower tower2, tower tower3)
{
    if (targetNum==1)
    {
        cout << "CURRENT ITEM: " << tower1.highest_ring_index << endl << "LOOKING FOR: " << tower1.max_ring_length << endl;
        if (tower1.highest_ring_index == tower1.max_ring_length){return true;}
        else {return false;}
    }
    else if (targetNum==2)
    {
        cout << "CURRENT ITEM: " << tower2.highest_ring_index << endl << "LOOKING FOR: " << tower2.max_ring_length << endl;
        if (tower2.highest_ring_index == tower2.max_ring_length){return true;}
        else {return false;}
    }
    else if (targetNum==3)
    {
        cout << "CURRENT ITEM: " << tower3.highest_ring_index << endl << "LOOKING FOR: " << tower3.max_ring_length << endl;
        if (tower3.highest_ring_index == tower3.max_ring_length){return true;}
        else {return false;}
    }
    return false;
}
void ring_loop(tower &tower1, tower &tower2, tower &tower3, int tower_target)
{
    int counter = 1;
    int row = 1, column = 1;
    bool run = true;
    while (run)
    {
        //SCREEN STUFF
        system("cls");
        cout << row << 'x' << column << "|" << counter << endl;
        
        //DISPLAYING
        display_rings(tower1, tower2, tower3);
        
        
        
        //BASIC COMMAND RUNNING BASED OFF OF ROWS AND COLUMNS
        if (row == 1)
        {
            if (column == 1) { cout << "rcntss" << endl; }
            if (column == 2) { swap_rings(tower1, tower2); }
            if (column == 3) { swap_rings(tower1, tower3); }
        }
        if (row == 2)
        {
            if (column == 1) { swap_rings(tower2, tower1); }
            if (column == 2) { cout << "rcntss" << endl; }
            if (column == 3) { swap_rings(tower2, tower3); }
        }
        if (row == 3)
        {
            if (column == 1) { swap_rings(tower3, tower1); }
            if (column == 2) { swap_rings(tower3, tower2); }
            if (column == 3) { cout << "rcntss" << endl; }
        }
        
        //UPDATING NUMBERS
        /* WHAT NEEDS TO BE CHECKED
         1. Default step is to update the column/row counter
         2. Check if the ring being transferred to the desired tower is more than 1 unit lower than the previous value
         -If so, either don't move it or keep note of the fact that it moved
         3. If the desired tower's current rings are lined perfectly (5,4,3)/etc
         -If so, do not modify the tower's rings
         -If not, continue to modify the ring
         */
        
        /*METHOD 1 -- SET PATH
         column++;
         if (column > 3) { row += 1; column = 1; }
         if (row > 3) { row = 1; column = 1; }
         cout << endl;
         */
        /*METHOD 2 -- RANDOM*/
        column = rand() % 3 + 1;
        row = rand() % 3 + 1;
        
        //CHECKING IF COMPLETE
        bool complete=check_if_complete(tower_target,tower1,tower2,tower3);
        
        if (complete){
            cout << "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" << endl;
            cout << "@@ using random method, puzzle completed in " << counter << " steps @@" << endl;
            cout << "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" << endl;
            return;
        }
        
        
        counter++;
        
    }
    
}
int main()
{
    //variable creation
    int ring_amount = 0, tower_target = 0, begin_tower = 0;
    
    //variable defining
    while ((ring_amount < 2) || (ring_amount > 100)) { cout << "How many rings? (2-10) "; cin >> ring_amount; }
    while ((begin_tower < 1) || (begin_tower > 3)) { cout << "Beginning tower? (1,2,3) "; cin >> begin_tower; }
    while ((tower_target < 1) || (tower_target > 3)) { cout << "Target tower? (1,2,3) "; cin >> tower_target; }
    
    //tower creation
    tower tower1((begin_tower == 1), ring_amount);
    tower tower2((begin_tower == 2), ring_amount);
    tower tower3((begin_tower == 3), ring_amount);
    
    /*DEBUG INPUTS
     tower2.remove_ring();
     tower2.remove_ring();
     tower2.remove_ring();
     tower2.add_ring(5); tower2.add_ring(4); tower2.add_ring(3); tower2.add_ring(2); tower2.add_ring(1);
     tower2.add_ring(); tower2.add_ring(3);
     tower2.display_array();*/
    
    //tower3.add_ring(5);
    ring_loop(tower1,tower2,tower3, tower_target);
    
    return 0;
}


#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n[10],a,i,j;
        cout<<"enter the no of friends:"<<endl;
        cin>>a;
        cout<<"enter the days"<<endl;
        for ( int i = 0 ; i< a ; i++)
        cin>>n[i];
        int count=a;

        
        for ( int j = 0 ; j< a ; j++){

            
            // int count=a-1;
            i=j;
            j++;
            for ( int i = 0 ; i< a ; i++)
            {
            // int count=a-1;
                // i++;
                if(i==j){
                count=count-1;
                i++;

              }
              break;

            }

        }
        // for ( int i = 0 ; i< a ; i++){
        //     int count=a-1;
        //     i++;
        // }
        
        cout<<"the number of friends he still have is "<<count<<endl;
    
     }

    return 0;
}
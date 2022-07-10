#include <iostream> 

using namespace std; 

 

int main() { 

int N, M, Q, q; cin>>N>>M; 

int m[N*M]; 

for(int i=0; i<(N*M); i++)cin>>m[i]; 

for(int i=0; i<(N*M)-1; i++){ 

  int menor=i; 

  for(int j=i+1; j<(N*M); j++){ 

    if(m[j]<m[menor])menor=j; 

  } 

  int aux=m[i]; 

    m[i]=m[menor]; 

    m[menor]=aux; 

} 

 

cin>>Q; 

for(int i=0; i<Q; i++){ 

  cin>>q; 

  int li=0, ls=(N*M)-1, meio; 

  while(li<=ls){ 

    meio=(li+ls)/2;  

    if(q<m[meio])ls=meio-1; 

    else if(q>m[meio])li=meio+1; 

    else break; 

  } 

  if(q==m[meio] && q!=m[meio+1]){ 

   cout<<meio+1<<endl; 

  } 

  else if(q==m[meio] && q==m[meio+1]){ 

    while (q==m[meio+1]){ 

      meio++; 

    } 

    cout<<meio+1<<endl; 

  } 

  else{ 

    if(m[meio]>q)cout<<meio<<endl; 

    else if(m[meio]<q)cout<<meio+1<<endl; 

  } 

 

} 

 return 0; 

}

//só deu assim KKKK
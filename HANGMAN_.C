#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<dos.h>
#include<graphics.h>
#include<stdlib.h>

//Logical error = if one letter is entered multiple time , It will still count as correct.
int j;
void hang();
void fig(int x);
void main(){
 /* FILE *fp;
  fp=fopen("HANGMAN_WORDS.TXT","r");
  if(fp==NULL)
  {  printf("File not found");
     delay(2000);
     exit(0);
     }
  else{
     printf("File found");
     delay(2000);
     }       */

  int i=0,m=0,l,n,chances,t,g,num_word[7]={0,0,0,0,0,0,0},w,r,num_letter_input[7];
  char str[]={"Theoran"},array_rep[7];
  char inp,mpercent,comp,gamew[]={"Congratulations You Won The Hangman Game"}; //would it be easy if we take a char instead of a string as input?
  clrscr();
 // fgets(str,7,fp);                      //comp variable to check during for loop
  n=strlen(str);
  g=strlen(gamew);
  chances=6;
  strlwr(str);
  hang();
  printf("\n\n\t\t\t WELCOME TO HANGMAN GAME ");
  printf("\n\t\t\t ______________________________ \n\n");
  printf("The word is %d word long.\nEnter & to see Game Rules.\nOr press any key to continue.\n",n);
  scanf("%c",&mpercent);
  if(mpercent=='&'){
    printf("Games Rules:\n1)First of all Enjoy this game\n2)The word has no repeating letters\n3)Entering a character twice will lead to penalty\n4)Enter character in small letter only\n");              //Prints Game Rules
  }
  while(1)
  {
    printf("\nEnter Letter\n");
    scanf("%c",&inp);


    if(chances<=0)
    {
      textcolor(RED + BLINK);
      cprintf("Game Over");      // checks if the player has ran out of chances or not!
      break;
    }
    else if((n-i)==0)
    {
      printf("Game has been Won");
      printf("\n\t\t\t\tWord is %s\n",strupr(str));
      for(l=0;l<g;l++){
	textcolor(l+1);
	cprintf("%c",gamew[l]);
	delay(500);
      }
      break;
    }
    else if(inp==10)      //to remove an error
    {
      continue;
    }
    for(w=0;w<7;w++){
    for(r=0;r<7;r++){
    if(str[r]==str[w]){
     num_word[r]++;
      }
    }
    }
     for(t=0;t<7;t++){
     if(array_rep[t]==inp)
     { num_letter_input[t]++;
      if(num_letter_input[t]>num_word[t])
       { printf("You have already Entered this letter twice.");
	 i--;
	 delay(1000);
	 chances--;
	 break;
       }

     }
    }
    for(t=0;t<n;t++)
    {
      if(inp==str[t])
      {
	//printf("Letter exists within the word");
	j=1;
	break;         //j will be used to transfer signals
      }

      else
      {
	//printf("Letter doesn't exist within the word");
	j=0;
       //printf("letter is %d",inp);       used for debugging
      }
   }

   if(j==1)
   { i++;
     fig(chances);
     if(j==1){
       printf("\n\n%c Letter matches\n",inp);      //This loops prevents this message to be printed after player loses the game
       printf("%d letters left \n\n",n-i);
       }
     array_rep[t]=inp;
     continue;
   }

   else if(j==0)
   { chances--;
     fig(chances);
     printf("\n\nLetter did not match\n");
     printf("%d letters left\n\n",n-i);
     //here it will send the signal to decrease the chance by 1
    // chances--;
     printf("Chances left %d\n",chances);
     continue;
   }
  }
  //fclose(fp);
  getch();
}

void hang()
 {
  printf("\t\t\tEnjoy Hangman\n\n\n");
  printf("\n\n\n\t\t%c%c%c%c  ",220,45,45,191);
  printf("\n\t\t%c  %c  ",222,179);
  printf("\n\t\t%c  %c\n\t\t%c  %c\n\t\t%c",222,179,222,179,222);
 }

void fig(int x)
{
 clrscr();
 textcolor(CYAN);
 if(x==6){
  hang();  }
 else if(x==5)    {
  hang();
  cprintf("  %c",2); }
 else if(x==4)           {
  hang();
  printf("  ");
  cprintf("%c",2);
  printf("\n\t\t  ");
  cprintf("%c",47);}
else if(x==3)            {
  hang();
  printf("  ");
  cprintf("%c",2);
  printf("\n\t\t  ");
  cprintf("%c",47);
  cprintf("%c",220);        }
else if(x==2)          {
  hang();
  printf("  ");
  cprintf("%c",2);
  printf("\n\t\t  ");
  cprintf("%c",47);
  cprintf("%c",220);
  cprintf("%c",92);       }
else if(x==1)            {
  hang();
  printf("  ");
  cprintf("%c",2);
  printf("\n\t\t  ");
  cprintf("%c",47);
  cprintf("%c",220);
  cprintf("%c",92);
  printf("\n\t\t  ");
  cprintf("%c",47); }
else if(x==0)           {
  hang();
  printf("  ");
  cprintf("%c",1);
  delay(1000);
  printf("\n\t\t  ");
  cprintf("%c",47);
  delay(1000);
  cprintf("%c",220);
  delay(1000);
  cprintf("%c",92);
  delay(1000);
  printf("\n\t\t  ");
  cprintf("%c",47);
  delay(1000);
  printf(" ");
  cprintf("%c",92);
  delay(1000);
  printf("\nYou are Hanged");
  j=10;   }
else
 {
 // printf("%d\n",x);
  printf("error");
  }
getch();
}
































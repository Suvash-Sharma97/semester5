#include <stdio.h>
#include <string.h>

void encrypt(char text[], int shift) {
    int i;
    char ch;
    
    for(i = 0; text[i] != '\0'; ++i) {
        ch = text[i];
        
        // Encrypt uppercase letters
        if(ch >= 'A' && ch <= 'Z') {
            ch = ch + shift;
            if(ch > 'Z') {
                ch = ch - 'Z' + 'A' - 1;
            }
            text[i] = ch;
        }
        // Encrypt lowercase letters
        else if(ch >= 'a' && ch <= 'z') {
            ch = ch + shift;
            if(ch > 'z') {
                ch = ch - 'z' + 'a' - 1;
            }
            text[i] = ch;
        }
        else if(ch >= '0' && ch <= '9') {
            ch = (ch - '0' + shift) % 10 + '0';
            text[i] = ch;
        }
        // Leave other characters (including whitespace) unchanged
    }
}

void decrypt(char text[], int shift) {
    int i;
    char ch;
    
    for(i = 0; text[i] != '\0'; ++i) {
        ch = text[i];
        
        // Decrypt uppercase letters
        if(ch >= 'A' && ch <= 'Z') {
            ch = ch - shift;
            if(ch < 'A') {
                ch = ch + 'Z' - 'A' + 1;
            }
            text[i] = ch;
        }
        // Decrypt lowercase letters
        else if(ch >= 'a' && ch <= 'z') {
            ch = ch - shift;
            if(ch < 'a') {
                ch = ch + 'z' - 'a' + 1;
            }
            text[i] = ch;
        }
        // Leave other characters (including whitespace) unchanged
    }
}

int main() {
    char text[100];
    int shift;
    int choice;
    
    printf("Enter a message: ");
    fgets(text, sizeof(text), stdin);
    
    printf("Enter shift: ");
    scanf("%d", &shift);
    
    // Remove newline character from fgets input
    int len = strlen(text);
    if (len > 0 && text[len-1] == '\n') {
        text[len-1] = '\0';
    }
    
    // Ask user for choice
    printf("Choose an option:\n");
    printf("1. Encrypt\n");
    printf("2. Decrypt\n");
    printf("Enter choice (1 or 2): ");
    scanf("%d", &choice);
    
    // Process based on user choice
    if (choice == 1) {
        encrypt(text, shift);
        printf("Encrypted message: %s\n", text);
    } else if (choice == 2) {
        decrypt(text, shift);
        printf("Decrypted message: %s\n", text);
    } else {
        printf("Invalid choice\n");
    }
    
    return 0;
}

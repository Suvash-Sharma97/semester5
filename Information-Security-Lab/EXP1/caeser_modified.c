#include <stdio.h>
#include <string.h>

char shift_char(char ch, int shift) {
    // Normalize shift
    int range;
    char base;

    if (ch >= 'A' && ch <= 'Z') {
        base = 'A';
        range = 26;
    } else if (ch >= 'a' && ch <= 'z') {
        base = 'a';
        range = 26;
    } else if (ch >= '0' && ch <= '9') {
        base = '0';
        range = 10;
    } else {
        return ch;  // Do not encrypt/decrypt non-alphanumeric characters
    }

    // Normalize the shift to be within 0 to range-1
    shift = ((shift % range) + range) % range;

    // Perform the shift
    return ((ch - base + shift) % range + range) % range + base;
}

// Function to process text with given shift
void process_text(char text[], int shift) {
    for (int i = 0; text[i] != '\0'; ++i) {
        text[i] = shift_char(text[i], shift);
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
        process_text(text, shift);
        printf("Encrypted message: %s\n", text);
    } else if (choice == 2) {
        process_text(text, -shift);
        printf("Decrypted message: %s\n", text);
    } else {
        printf("Invalid choice\n");
    }
    
    return 0;
}

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define GRID_SIZE 5
#define MAX_INPUT_SIZE 100

void create_grid(char key[], char grid[GRID_SIZE][GRID_SIZE]) {
    int alphabets[26] = {0};
    int key_len = strlen(key);
    int grid_index = 0;

    for (int i = 0; i < key_len; i++) {
        key[i] = tolower(key[i]);
        if (key[i] == 'j') {
            key[i] = 'i';
        }
        if (!alphabets[key[i] - 'a']) {
            alphabets[key[i] - 'a'] = 1;
        }
    }

    for (int i = 0; i < key_len; i++) {
        if (isalpha(key[i]) && alphabets[key[i] - 'a'] == 1) {
            grid[grid_index / GRID_SIZE][grid_index % GRID_SIZE] = key[i];
            alphabets[key[i] - 'a'] = 2;
            grid_index++;
        }
    }

    for (char ch = 'a'; ch <= 'z'; ch++) {
        if (ch == 'j') continue;
        if (alphabets[ch - 'a'] == 0) {
            grid[grid_index / GRID_SIZE][grid_index % GRID_SIZE] = ch;
            grid_index++;
        }
    }
}

void create_pairs(char plain_text[], char pairs[][2], int *num_pairs) {
    int text_len = strlen(plain_text);
    int index = 0;

    for (int i = 0; i < text_len; i++) {
        if (plain_text[i] == ' ') continue;
        if (index % 2 == 1 && plain_text[i] == pairs[index / 2][0]) {
            pairs[index / 2][index % 2] = 'x';
            index++;
        }
        pairs[index / 2][index % 2] = tolower(plain_text[i]);
        index++;
    }

    if (index % 2 == 1) {
        pairs[index / 2][1] = 'x';
        index++;
    }

    *num_pairs = index / 2;
}

void find_position(char letter, char grid[GRID_SIZE][GRID_SIZE], int *row, int *col) {
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (grid[i][j] == letter) {
                *row = i;
                *col = j;
                return;
            }
        }
    }
}

void encrypt_pairs(char pairs[][2], int num_pairs, char grid[GRID_SIZE][GRID_SIZE], char cipher_text[]) {
    int index = 0;

    for (int i = 0; i < num_pairs; i++) {
        int r1, c1, r2, c2;
        find_position(pairs[i][0], grid, &r1, &c1);
        find_position(pairs[i][1], grid, &r2, &c2);

        if (r1 == r2) {
            cipher_text[index++] = grid[r1][(c1 + 1) % GRID_SIZE];
            cipher_text[index++] = grid[r2][(c2 + 1) % GRID_SIZE];
        } else if (c1 == c2) {
            cipher_text[index++] = grid[(r1 + 1) % GRID_SIZE][c1];
            cipher_text[index++] = grid[(r2 + 1) % GRID_SIZE][c2];
        } else {
            cipher_text[index++] = grid[r1][c2];
            cipher_text[index++] = grid[r2][c1];
        }
    }

    cipher_text[index] = '\0';
}

void decrypt_pairs(char cipher_text[], char grid[GRID_SIZE][GRID_SIZE], char plain_text[]) {
    int text_len = strlen(cipher_text);
    int index = 0;

    for (int i = 0; i < text_len; i += 2) {
        int r1, c1, r2, c2;
        find_position(cipher_text[i], grid, &r1, &c1);
        find_position(cipher_text[i + 1], grid, &r2, &c2);

        if (r1 == r2) {
            plain_text[index++] = grid[r1][(c1 - 1 + GRID_SIZE) % GRID_SIZE];
            plain_text[index++] = grid[r2][(c2 - 1 + GRID_SIZE) % GRID_SIZE];
        } else if (c1 == c2) {
            plain_text[index++] = grid[(r1 - 1 + GRID_SIZE) % GRID_SIZE][c1];
            plain_text[index++] = grid[(r2 - 1 + GRID_SIZE) % GRID_SIZE][c2];
        } else {
            plain_text[index++] = grid[r1][c2];
            plain_text[index++] = grid[r2][c1];
        }
    }

    plain_text[index] = '\0';
}

int main() {
    char key[MAX_INPUT_SIZE];
    char text[MAX_INPUT_SIZE];
    char grid[GRID_SIZE][GRID_SIZE];
    char pairs[50][2];
    int num_pairs;
    char choice;

    printf("Enter the key: ");
    fgets(key, MAX_INPUT_SIZE, stdin);
    key[strcspn(key, "\n")] = 0; // Remove trailing newline

    printf("Do you want to encrypt (e) or decrypt (d)? ");
    scanf("%c", &choice);
    getchar(); // Consume the newline character left in the buffer

    if (choice == 'e' || choice == 'E') {
        printf("Enter the plain text: ");
        fgets(text, MAX_INPUT_SIZE, stdin);
        text[strcspn(text, "\n")] = 0; // Remove trailing newline

        create_grid(key, grid);
        create_pairs(text, pairs, &num_pairs);

        char cipher_text[100];
        encrypt_pairs(pairs, num_pairs, grid, cipher_text);

        printf("Cipher Text:\n%s\n", cipher_text);
    } else if (choice == 'd' || choice == 'D') {
        printf("Enter the cipher text: ");
        fgets(text, MAX_INPUT_SIZE, stdin);
        text[strcspn(text, "\n")] = 0; // Remove trailing newline

        create_grid(key, grid);

        char plain_text[100];
        decrypt_pairs(text, grid, plain_text);

        printf("Decrypted Text:\n%s\n", plain_text);
    } else {
        printf("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.\n");
    }

    return 0;
}

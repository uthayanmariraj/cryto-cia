#include <iostream>
#include <string>
using namespace std;

// Function to find gcd
int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

// Function to find modular inverse of a under mod 26
int modInverse(int a) {
    for (int x = 1; x < 26; x++) {
        if ((a * x) % 26 == 1)
            return x;
    }
    return -1; // no inverse
}

// Encryption function
string encrypt(string text, int key) {
    string result = "";

    for (char c : text) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            int p = c - base;
            int enc = (key * p) % 26;
            result += (enc + base);
        } else {
            result += c;
        }
    }
    return result;
}

// Decryption function
string decrypt(string text, int key) {
    string result = "";
    int inv = modInverse(key);

    if (inv == -1) {
        return "Invalid key! No modular inverse.";
    }

    for (char c : text) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            int c_val = c - base;
            int dec = (inv * c_val) % 26;
            result += (dec + base);
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    string text;
    int key;

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Enter key (a): ";
    cin >> key;

    if (gcd(key, 26) != 1) {
        cout << "Invalid key! Choose a number coprime with 26.\n";
        return 0;
    }

    string encrypted = encrypt(text, key);
    cout << "Encrypted: " << encrypted << endl;

    string decrypted = decrypt(encrypted, key);
    cout << "Decrypted: " << decrypted << endl;

    return 0;
}
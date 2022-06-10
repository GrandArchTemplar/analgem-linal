using namespace std;

#include <iostream>
#include <vector>

int main() {
	int vector_count;
	cout << "Enter vector count" << endl;
	cin >> vector_count;
	cout << "Enter vector matrix" << endl;
	double** vectors = new double* [vector_count];
	for (int i = 0; i < vector_count; i++) {
		vectors[i] = new double[vector_count];
	}
	for (int i = 0; i < vector_count; i++) {
		for (int j = 0; j < vector_count; j++) {
			cin >> vectors[i][j];
		}
	}
	int orthogonalization_step = 1;
	while (orthogonalization_step != vector_count) {
		for (int i = 0; i < orthogonalization_step; i++) {
			double ratio = 0;
			double ratio_up = 0;
			double ratio_down = 0;
			for (int j = 0; j < vector_count; j++) {
				ratio_up += vectors[j][orthogonalization_step] * vectors[j][orthogonalization_step - 1 - i];
				ratio_down += vectors[j][orthogonalization_step - 1 - i] * vectors[j][orthogonalization_step - 1 - i];
			}
			ratio = ratio_up / ratio_down;
			for (int j = 0; j < vector_count; j++) {
				if (ratio_up != 0.0 && ratio_down != 0.0) {
					vectors[j][orthogonalization_step] -= vectors[j][orthogonalization_step - 1 - i] * ratio;
				}
				else {
					break;
				}
			}
		}
		orthogonalization_step++;
	}
	cout << "Ortogonalization result" << endl;
	for (int i = 0; i < vector_count; i++) {
		for (int j = 0; j < vector_count; j++) {
			cout << vectors[i][j] << " ";
		}
		cout << endl;
	}
	for (int i = 0; i < vector_count; i++) {
		delete[] vectors[i];
	}
	delete[] vectors;
	return 0;
}
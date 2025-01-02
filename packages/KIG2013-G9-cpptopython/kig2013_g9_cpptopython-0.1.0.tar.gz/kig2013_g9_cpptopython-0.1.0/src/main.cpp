#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

tuple<vector<int>, vector<double>> numerical_analysis1(double sx, double sy, double t, double residual, double start) {
    double x = start;
    double xnext;
    int iter = 0;
    bool NotaNumber = false;
    vector<int> iters;
    vector<double> values;

    while (fabs(sy - x*t*sqrt(1-(sx*sx)/(x*x*t*t)) + 4.905*t*t) >= residual) {
        iters.push_back(iter);
        values.push_back(x);
        //cout << fixed << setprecision(4) << iter << ": " << x << endl;
        iter += 1;
        double f = sy - x*t*sqrt(1-(sx*sx)/(x*x*t*t)) + 4.905*t*t;
        double fprime = (-1*t)/sqrt(1-(sx/x/t)*(sx/x/t));
        xnext = x - f/fprime;
        x = xnext;
        if (isnan(fabs(sy - x*t*sqrt(1-(sx*sx)/(x*x*t*t)) + 4.905*t*t))) {
            NotaNumber = true;
        }
    }

    if (NotaNumber ==  true) {
        vector<int> vctempty1 = {};
        vector<double> vctempty2 = {};
        return make_tuple(vctempty1, vctempty2);
    } else {
        return make_tuple(iters, values);
    }
}

tuple<vector<int>, vector<double>> numerical_analysis2(double sx, double sy, double v, double residual, double start) {
    double x = start;
    double xnext;
    int iter = 0;
    bool NotaNumber = false;
    vector<int> iters;
    vector<double> values;

    while (fabs(sy - v*x*sqrt(1-(sx*sx)/(x*x*v*v)) + 4.905*x*x) >= residual) {
        iters.push_back(iter);
        values.push_back(x);
        //cout << fixed << setprecision(4) << iter << ": " << x << endl;
        iter += 1;
        double f = sy - v*x*sqrt(1-(sx*sx)/(x*x*v*v)) + 4.905*x*x;
        double fprime = 9.81*x - (sx*sx)/(v*x*x*sqrt(1 - (sx/v/x)*(sx/v/x))) - v*sqrt(1 - (sx/v/x)*(sx/v/x));
        xnext = x - f/fprime;
        x = xnext;
        if (isnan(fabs(sy - v*x*sqrt(1-(sx*sx)/(x*x*v*v)) + 4.905*x*x))) {
            NotaNumber = true;
        }
    }

    if (NotaNumber ==  true) {
        vector<int> vctempty1 = {};
        vector<double> vctempty2 = {};
        return make_tuple(vctempty1, vctempty2);
    } else {
        return make_tuple(iters, values);
    }
}

vector<double> eqn1(double sx, double v, double a, double t) {
    a = a*3.141592653589793 / 180;
    vector<double> vct = {sx, v, a, t};
    vector<int> imissing;
    for (int i = 0; i < 4; i++) {
        if (vct.at(i) == 0) {
            imissing.push_back(i);
        }
    }
    if (imissing.size() == 1) {
        if (imissing.at(0) == 0) {
            sx = v*cos(a)*t;
        } else if (imissing.at(0) == 1) {
            v = sx/(t*cos(a));
        } else if (imissing.at(0) == 2) {
            a = acos(sx/v/t);
            if (a == 0) a = 0.000000000000001;
        } else {
            t = sx/v/cos(a);
        }
        a = a*180 / 3.141592653589793;
        vct = {sx, v, a, t};
        return vct;
    } else if (imissing.size() == 0) {
        a = a*180 / 3.141592653589793;
        vct = {sx, v, a, t};
        return vct;
    } else {
        vct = {};
        return vct;
    }
}

vector<double> eqn2(double sy, double v, double a, double t) {
    a = a*3.141592653589793 / 180;
    vector<double> vct = {sy, v, a, t};
    vector<int> imissing;
    for (int i = 0; i < 4; i++) {
        if (vct.at(i) == 0) {
            imissing.push_back(i);
        }
    }
    if (imissing.size() == 1) {
        if (imissing.at(0) == 0) {
            sy = v*sin(a)*t - 4.905*t*t;
        } else if (imissing.at(0) == 1) {
            v = (sy + 4.905*t*t)/(t*sin(a));
        } else if (imissing.at(0) == 2) {
            a = asin((sy + 4.905*t*t)/v*t);
            if (a == 0) a = 0.000000000000001;
        } else {
            double A = 4.905;
            double B = v*sin(a);
            double C = sy;
            t = max((B - sqrt(B*B-4*A*C))/(2*A), (B + sqrt(B*B-4*A*C))/(2*A));
        }
        a = a*180 / 3.141592653589793;
        vct = {sy, v, a, t};
        return vct;
    } else if (imissing.size() == 0) {
        a = a*180 / 3.141592653589793;
        vct = {sy, v, a, t};
        return vct;
    } else {
        vct = {};
        return vct;
    }
}

vector<double> eqn3(double sx, double sy, double a, double t) {
    a = a*3.141592653589793 / 180;
    vector<double> vct = {sx, sy, a, t};
    vector<int> imissing;
    for (int i = 0; i < 4; i++) {
        if (vct.at(i) == 0) {
            imissing.push_back(i);
        }
    }
    if (imissing.size() == 1) {
        if (imissing.at(0) == 0) {
            sx = (sy + 4.905*t*t)/tan(a);
        } else if (imissing.at(0) == 1) {
            sy = sx*tan(a) - 4.905*t*t;
        } else if (imissing.at(0) == 2) {
            a = atan((sy + 4.905*t*t)/sx);
            if (a == 0) a = 0.000000000000001;
        } else {
            t = sqrt((sx*tan(a) - sy)/4.905);
        }
        a = a*180 / 3.141592653589793;
        vct = {sx, sy, a, t};
        return vct;
    } else if (imissing.size() == 0) {
        a = a*180 / 3.141592653589793;
        vct = {sx, sy, a, t};
        return vct;
    } else {
        vct = {};
        return vct;
    }
}

vector<double> eqn4(double sx, double sy, double v, double t) {
    vector<double> vct = {sx, sy, v, t};
    vector<int> imissing;
    for (int i = 0; i < 4; i++) {
        if (vct.at(i) == 0) {
            imissing.push_back(i);
        }
    }
    if (imissing.size() == 1) {
        if (imissing.at(0) == 2) {
            tuple<vector<int>, vector<double>> result = numerical_analysis1(sx, sy, t, 0.000000001, 2.0);
            if (get<1>(result).size() == 0) {
                v = -1;
            } else {
                v = get<1>(result)[get<1>(result).size() - 1];
            }
        } else if (imissing.at(0) == 3) {
            tuple<vector<int>, vector<double>> result = numerical_analysis2(sx, sy, v, 0.000000001, v + 1);
            if (get<1>(result).size() == 0) {
                t = -1;
            } else {
                t = get<1>(result)[get<1>(result).size() - 1];
            }
        }
        vct = {sx, sy, v, t};
        return vct;
    } else if (imissing.size() == 0) {
        vct = {sx, sy, v, t};
        return vct;
    } else {
        vct = {};
        return vct;
    }
}

vector<double> calculate(vector<double> inputs) {

    int fraud = 0;
    int fraud2 = 0;
    int zerocount = 0;
    if (inputs.size() == 5) {
        for (double num : inputs) {
            if (num == 0) zerocount += 1;
        }
        if (zerocount == 2) {
            vector<double> output1 = eqn1(inputs.at(0), inputs.at(2), inputs.at(3), inputs.at(4));
            vector<double> output2;
            if (output1.empty()) {
                vector<double> temp = eqn2(inputs.at(1), inputs.at(2), inputs.at(3), inputs.at(4));
                for (double num : temp) {
                    output2.push_back(num);
                }
                if (output2.empty()) {
                    vector<double> output3 = eqn3(inputs.at(0), inputs.at(1), inputs.at(3), inputs.at(4));
                    if (output3.empty()) {
                        vector<double> output4 = eqn4(inputs.at(0), inputs.at(1), inputs.at(2), inputs.at(4));
                        for (double num : output4) {
                            if (num == -1) {
                                fraud += 1;
                            }
                        }

                        if (fraud == 0) {
                            vector<double> temp2 = eqn2(output4.at(1), output4.at(2), 0.0, output4.at(3));
                            for (double num : temp2) {
                                output2.push_back(num);
                            }
                            vector<double> temp = eqn1(output4.at(0), output4.at(2), 0.0, output4.at(3));
                            for (double num : temp) {
                                output1.push_back(num);
                            }
                        }

                    } else {
                        vector<double> temp2 = eqn2(output3.at(1), 0.0, output3.at(2), output3.at(3));
                        for (double num : temp2) {
                            output2.push_back(num);
                        }
                        vector<double> temp = eqn1(output3.at(0), 0.0, output3.at(2), output3.at(3));
                        for (double num : temp) {
                            output1.push_back(num);
                        }
                    }
                } else {
                    output1 = eqn1(0.0, output2.at(1), output2.at(2), output2.at(3));
                }
            } else {
                vector<double> temp = eqn2(0.0, output1.at(1), output1.at(2), output1.at(3));
                for (double num : temp) {
                    output2.push_back(num);
                }
            }

            vector<double> outputs;
            if (fraud == 0) {
                vector<double> outputa = {output1.at(0), output2.at(0), output1.at(1), output1.at(2), output1.at(3)};
                vector<double> outputb = {output1.at(0), output2.at(0), output2.at(1), output2.at(2), output2.at(3)};
                for (int i = 0; i < 5; i++) {
                    if (isnan(outputa.at(i)) == false) {
                        outputs.push_back(outputa.at(i));
                    } else {
                        if (isnan(outputb.at(i)) == false) {
                            outputs.push_back(outputb.at(i));
                        } else {
                            fraud2 += 1;
                        }
                    }
                }
            } else {
                outputs.push_back(402);
            }

            if (fraud2 == 0) {
                return outputs;
            } else {
                vector<double> outputsbad = {403};
                return outputsbad;
            }
        } else {
            vector<double> outputsbad = {401};
            return outputsbad;
        }
    } else {
        vector<double> outputsbad = {400};
        return outputsbad;
    }
}

PYBIND11_MODULE(KIG2013_G9_cpptopython, m) {
    m.doc() = R"pbdoc(
        A demonstration of using C++ code
        in Python by packaging the former
        in a Python package using pybind11.

        ----------------------------------

        For use of:
        KIG2013 Programming Assignment

        ----------------------------------

        By:
        23006148/1 Kwong Ye Kun G9
    )pbdoc";

    m.def("calculate", &calculate, "A function which returns a vector.");
}
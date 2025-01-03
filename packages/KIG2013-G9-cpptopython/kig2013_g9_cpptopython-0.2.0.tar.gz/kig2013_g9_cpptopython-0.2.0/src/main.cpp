#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

//------------------------------------------ALL PURPOSE CALCULATOR---------------------------------------------

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

//--------------------------------TRAJECTORY OF BASKETBALL IN A 3D FORCE FIELD--------------------------------------

int checkval(string s) {
    int len = static_cast<int>(s.length());
    int fraud = 0;
    int dotpos = static_cast<int>(s.find("."));
    int minuspos = static_cast<int>(s.find("-"));
    if (dotpos != -1 && minuspos != -1) {
        if (dotpos == 0) {
            fraud += 1;
        }
        if (minuspos != 0) {
            fraud += 1;
        }
        if (dotpos == minuspos + 1) {
            fraud += 1;
        }
        if (dotpos == len - 1) {
            fraud += 1;
        }
        for (int i = 0; i < min(dotpos, minuspos); i++) {
            if (isdigit(s.at(i)) == 0) {
                fraud += 1;
            }
        }
        for (int i = min(dotpos, minuspos)+1; i < max(dotpos, minuspos); i++) {
            if (isdigit(s.at(i)) == 0) {
                fraud += 1;
            }
        }
        for (int i = max(dotpos, minuspos)+1; i < len; i++) {
            if (isdigit(s.at(i)) == 0) {
                fraud += 1;
            }
        }
    } else if (dotpos != -1 || minuspos != -1) {
        if (dotpos != -1) {
            if (dotpos == 0) {
                fraud += 1;
            } else {
                for (int i = 0; i < dotpos; i++) {
                    if (isdigit(s.at(i)) == 0) {
                        fraud += 1;
                    }
                }
                for (int i = dotpos+1; i < len; i++) {
                    if (isdigit(s.at(i)) == 0) {
                        fraud += 1;
                    }
                }
            }
        }
        if (minuspos != -1) {
            if (minuspos != 0) {
                fraud += 1;
            } else {
                for (int i = 1; i < len; i++) {
                    if (isdigit(s.at(i)) == 0) {
                        fraud += 1;
                    }
                }
            }
        }
    }
    if (dotpos == -1 && minuspos == -1) {
        for (int i = 0; i < len; i++) {
            if (isdigit(s.at(i)) == 0) {
                fraud += 1;
            }
        }
    }
    return fraud;
}

string replaceall(string str, string from, string to) {
    int pos = static_cast<int>(str.find(from, 0));
    while (pos != -1) {
        str.replace(pos, from.size(), to);
        pos = static_cast<int>(str.find(from, pos + from.size()));
    }
    pos = static_cast<int>(str.find(from, 0));
    if (pos != -1) str = replaceall(str, from, to);
    return str;
}

int nomeaning = 0;

vector<string> evaluate(string expr, int option1, int option2) {
    int fraud = checkval(expr);
    int notok = 0;
    if (fraud != 0) {
        expr = replaceall(expr, " ", "");
        expr = replaceall(expr, "++", "+");
        expr = replaceall(expr, "--", "+");
        expr = replaceall(expr, "+-", "-");
        expr = replaceall(expr, "-+", "-");
        if (expr.find("+") == 0) expr = expr.replace(0, 1, "");
        if (option1 == 1) cout << "= " << expr << endl;

        int xpos;
        if (static_cast<int>(expr.find("*")) == -1) {
            xpos = static_cast<int>(expr.find("x"));
        } else {
            xpos = static_cast<int>(expr.find("*"));
        }
        int dpos = static_cast<int>(expr.find("/"));
        int pos;
        string Id;

        string strdot = ".";
        string strminus = "-";
        string str0 = "0";
        string str1 = "1";
        string str2 = "2";
        string str3 = "3";
        string str4 = "4";
        string str5 = "5";
        string str6 = "6";
        string str7 = "7";
        string str8 = "8";
        string str9 = "9";

        if (xpos != -1 && dpos != -1) {
            if (xpos < dpos) {
                pos = xpos;
                Id = "x";
            } else {
                pos = dpos;
                Id = "/";
            }
        } else if (xpos == -1) {
            pos = dpos;
            Id = "/";
        } else {
            pos = xpos;
            Id = "x";
        }

        if (pos != -1) {
            int before = 0;
            int ibefore = pos - 1 - before;
            while (expr.at(ibefore) == str0.at(0) || expr.at(ibefore) == str1.at(0) || expr.at(ibefore) == str2.at(0) || expr.at(ibefore) == str3.at(0) || expr.at(ibefore) == str4.at(0) || expr.at(ibefore) == str5.at(0) || expr.at(ibefore) == str6.at(0) || expr.at(ibefore) == str7.at(0) || expr.at(ibefore) == str8.at(0) || expr.at(ibefore) == str9.at(0) || expr.at(ibefore) == strdot.at(0)) {
                before += 1;
                ibefore = pos - 1 - before;
                if (ibefore < 0) {
                    break;
                }
            }
            ibefore += 1;
            if (option2 == 1) cout << "Ibefore is: " << ibefore << endl;

            int after = 0;
            int iafter = pos + 1 + after;
            while (expr.at(iafter) == str0.at(0) || expr.at(iafter) == str1.at(0) || expr.at(iafter) == str2.at(0) || expr.at(iafter) == str3.at(0) || expr.at(iafter) == str4.at(0) || expr.at(iafter) == str5.at(0) || expr.at(iafter) == str6.at(0) || expr.at(iafter) == str7.at(0) || expr.at(iafter) == str8.at(0) || expr.at(iafter) == str9.at(0) || expr.at(iafter) == strdot.at(0) || expr.at(iafter) == strminus.at(0)) {
                after += 1;
                iafter = pos + 1 + after;
                if (iafter > static_cast<int>(expr.size()) - 1) {
                    break;
                }
                if (expr.at(iafter) == strminus.at(0) && after > 0) {
                    break;
                }
            }
            iafter -= 1;
            if (option2 == 1) cout << "Iafter is: " << iafter << endl;

            double firstnum = stod(expr.substr(ibefore, pos - ibefore));
            double secondnum = stod(expr.substr(pos + 1, iafter - pos));

            if (option2 == 1) cout << "First number is: " << firstnum << endl << "Second number is: " << secondnum << endl;

            string calc;
            (Id == "x") ? calc = to_string(firstnum * secondnum) : calc = to_string(firstnum / secondnum);

            if (option2 == 1) cout << "Result is: " << calc << endl;

            expr = expr.substr(0, ibefore) + calc + expr.substr(iafter + 1, expr.size() - iafter);
            if (option2 == 1) cout << "Next expression is: " << expr << endl;

            expr = (evaluate(expr, option1, option2))[0];
        }

        else {

            int ppos = static_cast<int>(expr.find("+"));
            int mpos = static_cast<int>(expr.find("-"));

            if (mpos == 0) {
                string newexpr = expr.substr(1, expr.size() - 1);
                mpos = static_cast<int>(newexpr.find("-"));
                if (mpos != -1) {
                    mpos += 1;
                }
            }

            if (ppos != -1 && mpos != -1) {
                if (ppos < mpos) {
                    pos = ppos;
                    Id = "+";
                } else {
                    pos = mpos;
                    Id = "-";
                }
            } else if (ppos == -1) {
                pos = mpos;
                Id = "-";
            } else {
                pos = ppos;
                Id = "+";
            }

            if (pos != -1) {

                int before = 0;
                int ibefore = pos - 1 - before;
                int minuscountb= 0;

                while (expr.at(ibefore) == str0.at(0) || expr.at(ibefore) == str1.at(0) || expr.at(ibefore) == str2.at(0) || expr.at(ibefore) == str3.at(0) || expr.at(ibefore) == str4.at(0) || expr.at(ibefore) == str5.at(0) || expr.at(ibefore) == str6.at(0) || expr.at(ibefore) == str7.at(0) || expr.at(ibefore) == str8.at(0) || expr.at(ibefore) == str9.at(0) || expr.at(ibefore) == strdot.at(0) || expr.at(ibefore) == strminus.at(0)) {
                    if (expr.at(ibefore) == strminus.at(0)) minuscountb += 1;
                    before += 1;
                    ibefore = pos - 1 - before;
                    if (ibefore < 0) {
                        break;
                    }
                    if (minuscountb > 1) {
                        break;
                    }
                }
                if (minuscountb > 1) {
                    ibefore += 3;
                } else {
                    ibefore += 1;
                }
                if (option2 == 1) cout << "Ibefore is: " << ibefore << endl;

                int after = 0;
                int iafter = pos + 1 + after;
                while (expr.at(iafter) == str0.at(0) || expr.at(iafter) == str1.at(0) || expr.at(iafter) == str2.at(0) || expr.at(iafter) == str3.at(0) || expr.at(iafter) == str4.at(0) || expr.at(iafter) == str5.at(0) || expr.at(iafter) == str6.at(0) || expr.at(iafter) == str7.at(0) || expr.at(iafter) == str8.at(0) || expr.at(iafter) == str9.at(0) || expr.at(iafter) == strdot.at(0)) {
                    after += 1;
                    iafter = pos + 1 + after;
                    if (iafter > static_cast<int>(expr.size()) - 1) {
                        break;
                    }
                }
                iafter -= 1;
                if (option2 == 1) cout << "Iafter is: " << iafter << endl;

                double firstnum = stod(expr.substr(ibefore, pos - ibefore));
                double secondnum = stod(expr.substr(pos + 1, iafter - pos));

                if (option2 == 1) cout << "First number is: " << firstnum << endl << "Second number is: " << secondnum << endl;

                string calc;
                (Id == "+") ? calc = to_string(firstnum + secondnum) : calc = to_string(firstnum - secondnum);

                if (option2 == 1) cout << "Result is: " << calc << endl;

                expr = expr.substr(0, ibefore) + calc + expr.substr(iafter + 1, expr.size() - iafter);
                if (option2 == 1) cout << "Next expression is: " << expr << endl;

                expr = (evaluate(expr, option1, option2))[0];

            }
            else {
                int fraud2 = checkval(expr);
                if (fraud2 != 0) {
                    nomeaning = 1;
                }
            }

        }
        if (option2 == 1) cout << "Pos is: " << pos << endl << "Id is: " << Id << endl;
    }

    vector<string> vctresult = {};
    vctresult.push_back(expr);
    vctresult.push_back(to_string(nomeaning));
    return vctresult;
}

vector<string> evalfunc(string func, double X, double Y, double Z) {
    nomeaning = 0;
    int faulty = 0;
    string str0 = "0";
    string str1 = "1";
    string str2 = "2";
    string str3 = "3";
    string str4 = "4";
    string str5 = "5";
    string str6 = "6";
    string str7 = "7";
    string str8 = "8";
    string str9 = "9";
    string strX = "X";
    string strY = "Y";
    string strZ = "Z";

    int Xpos = static_cast<int>(func.find("X"));
    while (Xpos != -1 && faulty == 0 && Xpos < static_cast<int>(func.size())) {
        if (Xpos != 0) {
            if (func.at(Xpos - 1) == str0.at(0) || func.at(Xpos - 1) == str1.at(0) || func.at(Xpos - 1) == str2.at(0) || func.at(Xpos - 1) == str3.at(0) || func.at(Xpos - 1) == str4.at(0) || func.at(Xpos - 1) == str5.at(0) || func.at(Xpos - 1) == str6.at(0) || func.at(Xpos - 1) == str7.at(0) || func.at(Xpos - 1) == str8.at(0) || func.at(Xpos - 1) == str9.at(0) || func.at(Xpos - 1) == strX.at(0) || func.at(Xpos - 1) == strY.at(0) || func.at(Xpos - 1) == strZ.at(0)) {
                faulty += 1;
            }
        }
        if (Xpos != static_cast<int>(func.size()) - 1) {
            if (func.at(Xpos + 1) == str0.at(0) || func.at(Xpos + 1) == str1.at(0) || func.at(Xpos + 1) == str2.at(0) || func.at(Xpos + 1) == str3.at(0) || func.at(Xpos + 1) == str4.at(0) || func.at(Xpos + 1) == str5.at(0) || func.at(Xpos + 1) == str6.at(0) || func.at(Xpos + 1) == str7.at(0) || func.at(Xpos + 1) == str8.at(0) || func.at(Xpos + 1) == str9.at(0) || func.at(Xpos + 1) == strX.at(0) || func.at(Xpos + 1) == strY.at(0) || func.at(Xpos + 1) == strZ.at(0)) {
                faulty += 1;
            }
            Xpos = static_cast<int>(func.find("X", Xpos + 1));
        } else {
            break;
        }
    }

    int Ypos = static_cast<int>(func.find("Y"));
    while (Ypos != -1 && faulty == 0 && Ypos < static_cast<int>(func.size())) {
        if (Ypos != 0) {
            if (func.at(Ypos - 1) == str0.at(0) || func.at(Ypos - 1) == str1.at(0) || func.at(Ypos - 1) == str2.at(0) || func.at(Ypos - 1) == str3.at(0) || func.at(Ypos - 1) == str4.at(0) || func.at(Ypos - 1) == str5.at(0) || func.at(Ypos - 1) == str6.at(0) || func.at(Ypos - 1) == str7.at(0) || func.at(Ypos - 1) == str8.at(0) || func.at(Ypos - 1) == str9.at(0) || func.at(Ypos - 1) == strX.at(0) || func.at(Ypos - 1) == strY.at(0) || func.at(Ypos - 1) == strZ.at(0)) {
                faulty += 1;
            }
        }
        if (Ypos != static_cast<int>(func.size()) - 1) {
            if (func.at(Ypos + 1) == str0.at(0) || func.at(Ypos + 1) == str1.at(0) || func.at(Ypos + 1) == str2.at(0) || func.at(Ypos + 1) == str3.at(0) || func.at(Ypos + 1) == str4.at(0) || func.at(Ypos + 1) == str5.at(0) || func.at(Ypos + 1) == str6.at(0) || func.at(Ypos + 1) == str7.at(0) || func.at(Ypos + 1) == str8.at(0) || func.at(Ypos + 1) == str9.at(0) || func.at(Ypos + 1) == strX.at(0) || func.at(Ypos + 1) == strY.at(0) || func.at(Ypos + 1) == strZ.at(0)) {
                faulty += 1;
            }
            Ypos = static_cast<int>(func.find("Y", Ypos + 1));
        } else {
            break;
        }
    }

    int Zpos = static_cast<int>(func.find("Z"));
    while (Zpos != -1 && faulty == 0 && Zpos < static_cast<int>(func.size())) {
        if (Zpos != 0) {
            if (func.at(Zpos - 1) == str0.at(0) || func.at(Zpos - 1) == str1.at(0) || func.at(Zpos - 1) == str2.at(0) || func.at(Zpos - 1) == str3.at(0) || func.at(Zpos - 1) == str4.at(0) || func.at(Zpos - 1) == str5.at(0) || func.at(Zpos - 1) == str6.at(0) || func.at(Zpos - 1) == str7.at(0) || func.at(Zpos - 1) == str8.at(0) || func.at(Zpos - 1) == str9.at(0) || func.at(Zpos - 1) == strX.at(0) || func.at(Zpos - 1) == strY.at(0) || func.at(Zpos - 1) == strZ.at(0)) {
                faulty += 1;
            }
        }
        if (Zpos != static_cast<int>(func.size()) - 1) {
            if (func.at(Zpos + 1) == str0.at(0) || func.at(Zpos + 1) == str1.at(0) || func.at(Zpos + 1) == str2.at(0) || func.at(Zpos + 1) == str3.at(0) || func.at(Zpos + 1) == str4.at(0) || func.at(Zpos + 1) == str5.at(0) || func.at(Zpos + 1) == str6.at(0) || func.at(Zpos + 1) == str7.at(0) || func.at(Zpos + 1) == str8.at(0) || func.at(Zpos + 1) == str9.at(0) || func.at(Zpos + 1) == strX.at(0) || func.at(Zpos + 1) == strY.at(0) || func.at(Zpos + 1) == strZ.at(0)) {
                faulty += 1;
            }
            Zpos = static_cast<int>(func.find("Z", Zpos + 1));
        } else {
            break;
        }
    }

    if (faulty == 0) {
        func = replaceall(func, "X", to_string(X));
        func = replaceall(func, "Y", to_string(Y));
        func = replaceall(func, "Z", to_string(Z));

        vector<string> vctresult;
        try {
            vctresult = evaluate(func, 0, 0);
        }
        catch (...) {
            vctresult = {};
            vctresult.push_back("0");
            vctresult.push_back("1");
        }
        return vctresult;
    } else {
        vector<string> vctresult;
        vctresult.push_back("0");
        vctresult.push_back("3");
        return vctresult;
    }
}

//-------------------------------------------CPP to PYTHON------------------------------------------------

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

    m.def("calculate", &calculate, "All purpose projectile motion calculator.");
    m.def("evalfunc", &evalfunc, "Evaluates the value of a multivariable function.");
    m.def("evaluate", &evaluate, "Evaluates the value of an expression.");
}
// This file is generated using functional_algorithms tool (0.13.3.dev1+g8d134ad.d20241230), see
//   https://github.com/pearu/functional_algorithms
// for more information.



#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <limits>


float acosh_0(float z) {
  float constant_f2 = 2.0;
  float constant_f1 = 1.0;
  float sqrt_subtract_z_constant_f1 = std::sqrt((z) - (constant_f1));
  return (((z) >= ((3.4028235e+38) / (constant_f2)))
              ? ((std::log(constant_f2)) + (std::log(z)))
              : (std::log1p((sqrt_subtract_z_constant_f1) *
                            ((std::sqrt((z) + (constant_f1))) +
                             (sqrt_subtract_z_constant_f1)))));
}

double acosh_1(double z) {
  double constant_f2 = 2.0;
  double constant_f1 = 1.0;
  double sqrt_subtract_z_constant_f1 = std::sqrt((z) - (constant_f1));
  return (((z) >= ((1.7976931348623157e+308) / (constant_f2)))
              ? ((std::log(constant_f2)) + (std::log(z)))
              : (std::log1p((sqrt_subtract_z_constant_f1) *
                            ((std::sqrt((z) + (constant_f1))) +
                             (sqrt_subtract_z_constant_f1)))));
}

std::complex<float> acosh_2(std::complex<float> z) {
  float signed_y = (z).imag();
  float y = std::abs(signed_y);
  float signed_x = (z).real();
  float x = std::abs(signed_x);
  float safe_max = (1.8446743e+19) / (8.0);
  float safe_max_opt =
      (((x) < ((safe_max) * (1000000000000.0))) ? ((safe_max) * (1e-06))
                                                : ((safe_max) * (100.0)));
  bool y_gt_safe_max_opt = (y) >= (safe_max_opt);
  float mx = ((y_gt_safe_max_opt) ? (y) : (x));
  float two = 2.0;
  float half = 0.5;
  float zero = 0.0;
  float xoy = (((y_gt_safe_max_opt) &&
                (!((y) == (std::numeric_limits<float>::infinity()))))
                   ? ((x) / (y))
                   : (zero));
  float one = 1.0;
  bool logical_and_lt_y_safe_min_lt_x_one =
      ((y) < (4.3368087e-19)) && ((x) < (one));
  float xp1 = (x) + (one);
  float xm1 = (x) - (one);
  float abs_xp1 = std::abs(xp1);
  float _mx_0_ = std::max(abs_xp1, y);
  float mn = std::min(abs_xp1, y);
  float sqrt_two = 1.4142135;
  float mn_over_mx = (mn) / (_mx_0_);
  float _r_0_ = (mn_over_mx) * (mn_over_mx);
  float sqa = std::sqrt((one) + (_r_0_));
  float r =
      (((_mx_0_) == (mn)) ? ((sqrt_two) * (_mx_0_))
                          : (((((sqa) == (one)) && ((_r_0_) > (zero)))
                                  ? ((_mx_0_) + (((_mx_0_) * (_r_0_)) / (two)))
                                  : ((_mx_0_) * (sqa)))));
  float abs_xm1 = std::abs(xm1);
  float _mx_1_ = std::max(abs_xm1, y);
  float _mn_0_ = std::min(abs_xm1, y);
  float _mn_over_mx_0_ = (_mn_0_) / (_mx_1_);
  float _r_1_ = (_mn_over_mx_0_) * (_mn_over_mx_0_);
  float _sqa_0_ = std::sqrt((one) + (_r_1_));
  float s = (((_mx_1_) == (_mn_0_))
                 ? ((sqrt_two) * (_mx_1_))
                 : (((((_sqa_0_) == (one)) && ((_r_1_) > (zero)))
                         ? ((_mx_1_) + (((_mx_1_) * (_r_1_)) / (two)))
                         : ((_mx_1_) * (_sqa_0_)))));
  float a = (half) * ((r) + (s));
  float ap1 = (a) + (one);
  float yy = (y) * (y);
  float half_yy = (half) * (yy);
  float rpxp1 = (r) + (xp1);
  float divide_half_yy_rpxp1 = (half_yy) / (rpxp1);
  float spxm1 = (s) + (xm1);
  float smxm1 = (s) - (xm1);
  float x_ge_1_or_not =
      (((x) >= (one))
           ? ((divide_half_yy_rpxp1) + ((half) * (spxm1)))
           : ((((a) <= (1.5)) ? ((divide_half_yy_rpxp1) + ((half_yy) / (smxm1)))
                              : ((a) - (one)))));
  float am1 =
      ((logical_and_lt_y_safe_min_lt_x_one) ? (-(((xp1) * (xm1)) / (ap1)))
                                            : (x_ge_1_or_not));
  float sq = std::sqrt((am1) * (ap1));
  float half_apx = (half) * ((a) + (x));
  float _imag_0_ = std::atan2(
      (((std::max(x, y)) >= (safe_max))
           ? (y)
           : ((((x) <= (one))
                   ? (std::sqrt((half_apx) * (((yy) / (rpxp1)) + (smxm1))))
                   : ((y) * (std::sqrt(((half_apx) / (rpxp1)) +
                                       ((half_apx) / (spxm1)))))))),
      signed_x);
  return std::complex<float>(
      (((mx) >= (((y_gt_safe_max_opt) ? (safe_max_opt) : (safe_max))))
           ? (((std::log(two)) + (std::log(mx))) +
              ((half) * (std::log1p((xoy) * (xoy)))))
           : (((logical_and_lt_y_safe_min_lt_x_one)
                   ? ((y) / (sq))
                   : (std::log1p((am1) + (sq)))))),
      (((signed_y) < (0.0)) ? (-(_imag_0_)) : (_imag_0_)));
}

std::complex<double> acosh_3(std::complex<double> z) {
  double signed_y = (z).imag();
  double y = std::abs(signed_y);
  double signed_x = (z).real();
  double x = std::abs(signed_x);
  double safe_max = (1.3407807929942596e+154) / (8.0);
  double safe_max_opt =
      (((x) < ((safe_max) * (1000000000000.0))) ? ((safe_max) * (1e-06))
                                                : ((safe_max) * (100.0)));
  bool y_gt_safe_max_opt = (y) >= (safe_max_opt);
  double mx = ((y_gt_safe_max_opt) ? (y) : (x));
  double two = 2.0;
  double half = 0.5;
  double zero = 0.0;
  double xoy = (((y_gt_safe_max_opt) &&
                 (!((y) == (std::numeric_limits<double>::infinity()))))
                    ? ((x) / (y))
                    : (zero));
  double one = 1.0;
  bool logical_and_lt_y_safe_min_lt_x_one =
      ((y) < (5.966672584960166e-154)) && ((x) < (one));
  double xp1 = (x) + (one);
  double xm1 = (x) - (one);
  double abs_xp1 = std::abs(xp1);
  double _mx_0_ = std::max(abs_xp1, y);
  double mn = std::min(abs_xp1, y);
  double sqrt_two = 1.4142135623730951;
  double mn_over_mx = (mn) / (_mx_0_);
  double _r_0_ = (mn_over_mx) * (mn_over_mx);
  double sqa = std::sqrt((one) + (_r_0_));
  double r =
      (((_mx_0_) == (mn)) ? ((sqrt_two) * (_mx_0_))
                          : (((((sqa) == (one)) && ((_r_0_) > (zero)))
                                  ? ((_mx_0_) + (((_mx_0_) * (_r_0_)) / (two)))
                                  : ((_mx_0_) * (sqa)))));
  double abs_xm1 = std::abs(xm1);
  double _mx_1_ = std::max(abs_xm1, y);
  double _mn_0_ = std::min(abs_xm1, y);
  double _mn_over_mx_0_ = (_mn_0_) / (_mx_1_);
  double _r_1_ = (_mn_over_mx_0_) * (_mn_over_mx_0_);
  double _sqa_0_ = std::sqrt((one) + (_r_1_));
  double s = (((_mx_1_) == (_mn_0_))
                  ? ((sqrt_two) * (_mx_1_))
                  : (((((_sqa_0_) == (one)) && ((_r_1_) > (zero)))
                          ? ((_mx_1_) + (((_mx_1_) * (_r_1_)) / (two)))
                          : ((_mx_1_) * (_sqa_0_)))));
  double a = (half) * ((r) + (s));
  double ap1 = (a) + (one);
  double yy = (y) * (y);
  double half_yy = (half) * (yy);
  double rpxp1 = (r) + (xp1);
  double divide_half_yy_rpxp1 = (half_yy) / (rpxp1);
  double spxm1 = (s) + (xm1);
  double smxm1 = (s) - (xm1);
  double x_ge_1_or_not =
      (((x) >= (one))
           ? ((divide_half_yy_rpxp1) + ((half) * (spxm1)))
           : ((((a) <= (1.5)) ? ((divide_half_yy_rpxp1) + ((half_yy) / (smxm1)))
                              : ((a) - (one)))));
  double am1 =
      ((logical_and_lt_y_safe_min_lt_x_one) ? (-(((xp1) * (xm1)) / (ap1)))
                                            : (x_ge_1_or_not));
  double sq = std::sqrt((am1) * (ap1));
  double half_apx = (half) * ((a) + (x));
  double _imag_0_ = std::atan2(
      (((std::max(x, y)) >= (safe_max))
           ? (y)
           : ((((x) <= (one))
                   ? (std::sqrt((half_apx) * (((yy) / (rpxp1)) + (smxm1))))
                   : ((y) * (std::sqrt(((half_apx) / (rpxp1)) +
                                       ((half_apx) / (spxm1)))))))),
      signed_x);
  return std::complex<double>(
      (((mx) >= (((y_gt_safe_max_opt) ? (safe_max_opt) : (safe_max))))
           ? (((std::log(two)) + (std::log(mx))) +
              ((half) * (std::log1p((xoy) * (xoy)))))
           : (((logical_and_lt_y_safe_min_lt_x_one)
                   ? ((y) / (sq))
                   : (std::log1p((am1) + (sq)))))),
      (((signed_y) < (0.0)) ? (-(_imag_0_)) : (_imag_0_)));
}
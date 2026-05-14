#!/usr/bin/env python3
import argparse, math

def cohens_kappa(agreed, disagreed):
    n = agreed + disagreed
    p_obs = agreed / n if n > 0 else 0
    p_pos = ((agreed / 2 + disagreed/4) / n) ** 2 if n > 0 else 0
    p_neg = ((agreed / 2 + disagreed/4) / n) ** 2 if n > 0 else 0
    p_exp = p_pos + p_neg
    if p_exp >= 1:
        return 1.0, 0
    kappa = (p_obs - p_exp) / (1 - p_exp)
    se = math.sqrt((p_obs * (1 - p_obs)) / (n * (1 - p_exp) ** 2)) if n > 0 else 0
    return kappa, se

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate Cohen\'s Kappa for inter-rater agreement')
    parser.add_argument('--agreed', type=int, required=True, help='Number of agreements')
    parser.add_argument('--disagreed', type=int, required=True, help='Number of disagreements')
    args = parser.parse_args()
    k, se = cohens_kappa(args.agreed, args.disagreed)
    print(f"Cohen's κ: {k:.3f}")
    print(f"SE: {se:.3f}")
    print(f"Agreement: {args.agreed}/{args.agreed + args.disagreed} ({100*args.agreed/(args.agreed+args.disagreed):.1f}%)")
    if k > 0.80:
        print("Interpretation: Excellent agreement — proceed")
    elif k > 0.60:
        print("Interpretation: Good agreement — brief calibration recommended")
    elif k > 0.40:
        print("Interpretation: Moderate agreement — stop and recalibrate")
    else:
        print("Interpretation: Poor agreement — re-pilot with refined criteria")

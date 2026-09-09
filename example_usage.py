from client import RiemannianSphereOptimizer

def main():
    print("=== Riemannian Sphere Manifold Optimizer ===")
    opt = RiemannianSphereOptimizer()
    pt = [1.0, 0.0, 0.0]
    grad = [1.0, 2.0, 0.0]

    res = opt.step(pt, grad, lr=0.1)
    print("Riemannian Step Result:", res)
    assert res["on_manifold"] is True

    print("Riemannian Sphere Optimizer verified successfully!")

if __name__ == "__main__":
    main()

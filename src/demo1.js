import { Component } from "@/components/ui/interactive-3d-cube-grid";

const DemoOne = () => {
  return (
    <div className="flex w-full h-screen justify-center items-center">
      <Component 
        gridSize={8}
        maxAngle={60}
        radius={4}
        borderStyle="2px dashed #5227FF"
        faceColor="#1a1a2e"
        rippleColor="#ff6b6b"
        rippleSpeed={1.5}
        autoAnimate={true}
        rippleOnClick={true}
      />
    </div>
  );
};

export { DemoOne };
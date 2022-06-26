import main as main
import render as render
main.startSoftware()
renderInstance = render.Render()
renderInstance.packRender()
renderInstance.mainLoop()

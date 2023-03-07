#version 430

out vec4 fragColor;

uniform vec2 resolution;
uniform float time;
uniform vec2 move;

void main() {
    vec2 uv = gl_FragCoord.xy / resolution.xy - move.xy;
    vec4 color = vec4(0.0, 0.0, 0.0, 1.0);

        if (abs(uv.x - 0.5) < 0.15 && abs(uv.y - 0.5) < 0.15 && abs((uv.x + uv.y) * (time / 8)) < 0.1) {
            color += vec4(0, 1.0, 0, 1.0);
            fragColor = color;
        }
        else {
            fragColor = vec4(0.0, 0.0, 0.0, 1.0);
        }
}
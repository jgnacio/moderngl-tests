#version 430

out vec4 fragColor;

uniform vec2 resolution;
uniform float time;
uniform vec2 move;

void main() {
    vec2 uv = (gl_FragCoord.xy - 0.5 * resolution.xy) / resolution.xy - move.xy;
    vec3 col = vec3(0.0);

    col +=  0.01 / length(uv);

    fragColor = vec4(col, 1.0);
}
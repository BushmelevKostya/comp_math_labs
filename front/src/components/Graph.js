import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

function Graph( {currentGraph, setCurrentGraph} ) {
    const chartRef = useRef(null);
    const chartInstanceRef = useRef(null);

    useEffect(() => {
        if (chartInstanceRef.current) {
            chartInstanceRef.current.destroy();
        }

        const ctx = chartRef.current.getContext('2d');
        chartInstanceRef.current = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Array.from({ length: 100 }, (_, i) => i + 1),
                datasets: [{
                    label: 'y = x^2',
                    data: Array.from({ length: 100 }, (_, i) => Math.pow(i + 1, 2)),
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    fill: false
                }]
            },
            options: {
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'x'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'y'
                        }
                    }
                }
            }
        });

        return () => {
            if (chartInstanceRef.current) {
                chartInstanceRef.current.destroy();
            }
        };
    }, []);

    return (
        <div>
            <canvas ref={chartRef} width="400" height="400"></canvas>
        </div>
    );
}

export default Graph;

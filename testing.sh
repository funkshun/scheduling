#!/usr/bin/env bash

echo ""
echo "=== Test 1: EDF vs. non-preemptive EDF ==="
echo "  EDF schedule generation"
python EDF.py test1.json test1_EDF.json
python visualizer.py test1_EDF.json
ps2pdf schedule.ps test1_EDF.pdf
pdfcrop test1_EDF.pdf test1_EDF.pdf
rm schedule.ps
echo "  non-preemptive EDF schedule generation"
 python nonPreemptiveEDF.py test1.json test1_np-EDF.json
 python visualizer.py test1_np-EDF.json
 ps2pdf schedule.ps test1_np-EDF.pdf
 pdfcrop test1_np-EDF.pdf test1_np-EDF.pdf
 rm schedule.ps

# echo ""
# echo "=== Test 2: EDF vs. RM ==="
# echo "  EDF schedule generation"
# python EDF.py test2.json test2_EDF.json
# python visualizer.py test2_EDF.json
# ps2pdf schedule.ps test2_EDF.pdf
# pdfcrop test2_EDF.pdf test2_EDF.pdf
# rm schedule.ps
# echo "  RM schedule generation"
# python RM.py test2.json test2_RM.json
# python visualizer.py test2_RM.json
# ps2pdf schedule.ps test2_RM.pdf
# pdfcrop test2_RM.pdf test2_RM.pdf
# rm schedule.ps

# echo ""
# echo "=== Test 3: RM vs. DM ==="
# echo "  RM schedule generation"
# python RM.py test3.json test3_RM.json
# python visualizer.py test3_RM.json
# ps2pdf schedule.ps test3_RM.pdf
# pdfcrop test3_RM.pdf test3_RM.pdf
# rm schedule.ps
# echo "  DM schedule generation"
# python DM.py test3.json test3_DM.json
# python visualizer.py test3_DM.json
# ps2pdf schedule.ps test3_DM.pdf
# pdfcrop test3_DM.pdf test3_DM.pdf
# rm schedule.ps

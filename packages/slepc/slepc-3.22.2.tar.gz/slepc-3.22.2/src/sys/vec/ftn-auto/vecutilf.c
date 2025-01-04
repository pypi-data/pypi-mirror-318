#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* vecutil.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcvec.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define vecnormalizecomplex_ VECNORMALIZECOMPLEX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define vecnormalizecomplex_ vecnormalizecomplex
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define veccheckorthogonality_ VECCHECKORTHOGONALITY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define veccheckorthogonality_ veccheckorthogonality
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define veccheckorthonormality_ VECCHECKORTHONORMALITY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define veccheckorthonormality_ veccheckorthonormality
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define vecduplicateempty_ VECDUPLICATEEMPTY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define vecduplicateempty_ vecduplicateempty
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define vecsetrandomnormal_ VECSETRANDOMNORMAL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define vecsetrandomnormal_ vecsetrandomnormal
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  vecnormalizecomplex_(Vec xr,Vec xi,PetscBool *iscomplex,PetscReal *norm, int *ierr)
{
CHKFORTRANNULLOBJECT(xr);
CHKFORTRANNULLOBJECT(xi);
CHKFORTRANNULLREAL(norm);
*ierr = VecNormalizeComplex(
	(Vec)PetscToPointer((xr) ),
	(Vec)PetscToPointer((xi) ),*iscomplex,norm);
}
SLEPC_EXTERN void  veccheckorthogonality_(Vec V[],PetscInt *nv,Vec W[],PetscInt *nw,Mat B,PetscViewer viewer,PetscReal *lev, int *ierr)
{
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
PetscBool W_null = !*(void**) W ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(W);
CHKFORTRANNULLOBJECT(B);
CHKFORTRANNULLOBJECT(viewer);
CHKFORTRANNULLREAL(lev);
*ierr = VecCheckOrthogonality(V,*nv,W,*nw,
	(Mat)PetscToPointer((B) ),PetscPatchDefaultViewers((PetscViewer*)viewer),lev);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! W_null && !*(void**) W) * (void **) W = (void *)-2;
}
SLEPC_EXTERN void  veccheckorthonormality_(Vec V[],PetscInt *nv,Vec W[],PetscInt *nw,Mat B,PetscViewer viewer,PetscReal *lev, int *ierr)
{
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
PetscBool W_null = !*(void**) W ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(W);
CHKFORTRANNULLOBJECT(B);
CHKFORTRANNULLOBJECT(viewer);
CHKFORTRANNULLREAL(lev);
*ierr = VecCheckOrthonormality(V,*nv,W,*nw,
	(Mat)PetscToPointer((B) ),PetscPatchDefaultViewers((PetscViewer*)viewer),lev);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! W_null && !*(void**) W) * (void **) W = (void *)-2;
}
SLEPC_EXTERN void  vecduplicateempty_(Vec v,Vec *newv, int *ierr)
{
CHKFORTRANNULLOBJECT(v);
PetscBool newv_null = !*(void**) newv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newv);
*ierr = VecDuplicateEmpty(
	(Vec)PetscToPointer((v) ),newv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newv_null && !*(void**) newv) * (void **) newv = (void *)-2;
}
SLEPC_EXTERN void  vecsetrandomnormal_(Vec v,PetscRandom rctx,Vec w1,Vec w2, int *ierr)
{
CHKFORTRANNULLOBJECT(v);
CHKFORTRANNULLOBJECT(rctx);
CHKFORTRANNULLOBJECT(w1);
CHKFORTRANNULLOBJECT(w2);
*ierr = VecSetRandomNormal(
	(Vec)PetscToPointer((v) ),
	(PetscRandom)PetscToPointer((rctx) ),
	(Vec)PetscToPointer((w1) ),
	(Vec)PetscToPointer((w2) ));
}
#if defined(__cplusplus)
}
#endif
